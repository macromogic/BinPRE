import argparse
import socket
import time
from dataclasses import dataclass
from pathlib import Path
from scapy.all import rdpcap


@dataclass
class Config:
    host: str
    port: int
    udp: bool = False
    needs_reconnect: bool = False
    bind_port: int = None

    @property
    def ip_port(self):
        return self.host, self.port

    @classmethod
    def from_protocol(cls, host, protocol):
        match protocol:
            case 'modbus':
                return cls(host=host, port=502)
            case 'tftp':
                return cls(host=host, port=69, udp=True, bind_port=7788)
            case 'http':
                return cls(host=host, port=80, needs_reconnect=True)
            case 'dns':
                return cls(host=host, port=53, udp=True)
            case 'dnp3':
                return cls(host=host, port=20000)
            case 'eip':
                return cls(host=host, port=44818)
            case 'mirai':
                return cls(host=host, port=43608, bind_port=23)
            case 'dnp3':
                return cls(host=host, port=20000)
            case 's7':
                return cls(host=host, port=102)
            case 'ftp':
                return cls(host=host, port=21)
            case _:
                raise ValueError(f"Unknown protocol: {protocol}")


def connect(ip_port, udp=False, bind_port=None, timeout=2):
    if udp:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    else:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    if bind_port:
        sock.bind(('', bind_port))
        print(f"Listening on port {bind_port} for {'UDP' if udp else 'TCP'}")
        if not udp:
            sock.listen()
            sock, (addr, port) = sock.accept()
            print(f"Accepted connection from {addr}:{port}")
    else:
        sock.connect(ip_port)
        print(f"Established {'UDP' if udp else 'TCP'} connection to {ip_port}")
    sock.settimeout(timeout)
    return sock


def get_payload(pcap_path, port, udp, num_requests):
    pcap_path = pcap_path.as_posix()
    raw_packets = rdpcap(pcap_path)
    payloads = []
    proto = 'UDP' if udp else 'TCP'
    for packet in raw_packets:
        if not packet.haslayer(proto):
            continue
        layer = packet[proto]
        if layer.dport == port and (payload := layer.payload.build()):
            payloads.append(payload)
    if num_requests > 0:
        payloads = payloads[:num_requests]
    return payloads


def hexdump(data, limit=-1):
    if limit > 0 and len(data) > limit:
        truncated = len(data) - limit
        data = data[:limit]
    else:
        truncated = 0
    result = []
    for i in range(0, len(data), 16):
        s = data[i:i+16]
        hexa = ' '.join([f"{c:02x}" for c in s])
        text = ''.join([chr(c) if 32 <= c < 127 else '.' for c in s])
        result.append(f"{hexa:<48} {text}")
    if truncated:
        result.append(f"... ({truncated} more bytes)")
    return '\n'.join(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('protocol', type=str)
    parser.add_argument('--host', '-H', type=str, default='127.0.0.1')
    parser.add_argument('--port', '-p', type=int)
    parser.add_argument('--num-requests', '-n', type=int, default=-1)
    parser.add_argument('--timeout', '-t', type=int, default=2)
    parser.add_argument('--input', '-i', type=Path)
    parser.add_argument('--num-retries', '-r', type=int, default=10)
    parser.add_argument('--verbose-limit', '-l', type=int, default=256)
    parser.add_argument('--no-response', '-nore', action='store_true')
    parser.add_argument('--dump', '-d', type=argparse.FileType('w'), default=None)
    args = parser.parse_args()

    protocol = args.protocol.lower()
    if not (pcap_path := args.input):
        binpre_dir = Path(__file__).absolute().parent.parent.parent
        pcap_path = binpre_dir / 'Analyzer' / 'pcaps' / f'{protocol}_50.pcap'
    config = Config.from_protocol(args.host or '127.0.0.1', protocol)
    if args.port:
        config.port = args.port

    payloads = get_payload(pcap_path, config.port, config.udp, args.num_requests)
    if fdump := args.dump:
        for payload in payloads:
            fdump.write(payload.hex().upper() + '\n')
        return
    print(f"Loaded {len(payloads)} payloads from {pcap_path}")
    sock = connect(config.ip_port, config.udp, bind_port=config.bind_port, timeout=args.timeout)
    for i, payload in enumerate(payloads, 1):
        print(f"Sending payload {i}/{len(payloads)} of size {len(payload)}:\n{hexdump(payload, args.verbose_limit)}")
        if config.udp:
            sock.sendto(payload, config.ip_port)
        else:
            sock.send(payload)
        response = b''
        reason = f'max retries ({args.num_retries})'
        for _ in range(args.num_retries):
            try:
                if response := sock.recv(255):
                    # print(hexdump(response))
                    while chunk := sock.recv(255):
                        response += chunk
                        # print(hexdump(chunk))
                    break
            except socket.timeout:
                reason = 'timeout'
                break
            time.sleep(0.5)
        if response:
            print(f"Received response of size {len(response)}:\n{hexdump(response, args.verbose_limit)}")
        else:
            if args.no_response:
                print(f"No response received after {reason}")
            else:
                raise RuntimeError(f"No response received after {reason}")
        if config.needs_reconnect:
            sock.close()
            sock = connect(config.ip_port, config.udp, bind_port=config.bind_port, timeout=args.timeout)
    sock.close()


if __name__ == '__main__':
    main()
