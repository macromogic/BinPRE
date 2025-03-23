import argparse
import socket
import time
from pathlib import Path
from scapy.all import rdpcap


def protocol_config(protocol):
    match protocol:
        case 'modbus':
            return 502, False
        case 'tftp':
            return 69, True
        case 'http':
            return 80, False
        case 'dns':
            return 53, True
        case 'dnp3':
            return 20000, False
        case _:
            raise ValueError(f"Unknown protocol: {protocol}")


def connect(ip_port, udp=False, timeout=2):
    if udp:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    else:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.settimeout(timeout)
    sock.connect(ip_port)
    print(f"Connected to {ip_port}")
    return sock


def get_payload(pcap_path, port, udp, num_requests):
    raw_packets = rdpcap(pcap_path.as_posix())
    payloads = []
    layer = 'UDP' if udp else 'TCP'
    for packet in raw_packets:
        if not packet.haslayer(layer):
            continue
        layer = packet[layer]
        if layer.dport == port and (payload := layer.payload.build()):
            payloads.append(payload)
    if num_requests > 0:
        payloads = payloads[:num_requests]
    print(f"Loaded {len(payloads)} payloads")
    return payloads


def hexdump(data):
    result = []
    for i in range(0, len(data), 16):
        s = data[i:i+16]
        hexa = ' '.join([f"{c:02x}" for c in s])
        text = ''.join([chr(c) if 32 <= c < 127 else '.' for c in s])
        result.append(f"{hexa:<48} {text}")
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
    args = parser.parse_args()

    protocol = args.protocol.lower()
    if not (pcap_path := args.input):
        binpre_dir = Path(__file__).absolute().parent.parent.parent
        pcap_path = binpre_dir / 'Analyzer' / 'pcaps' / f'{protocol}_50.pcap'
    port, is_udp = protocol_config(protocol)
    ip_port = (args.host, args.port or port)

    payloads = get_payload(pcap_path, port, is_udp, args.num_requests)
    sock = connect(ip_port, is_udp, args.timeout)
    for i, payload in enumerate(payloads, 1):
        print(f"Sending payload {i}/{len(payloads)} of size {len(payload)}:\n{hexdump(payload)}")
        if is_udp:
            sock.sendto(payload, ip_port)
        else:
            sock.send(payload)
        response = b''
        for _ in range(args.num_retries):
            if response := sock.recv(255):
                break
            time.sleep(0.5)
        if response:
            print(f"Received response of size {len(response)}:\n{hexdump(response)}")
        else:
            raise RuntimeError(f"No response received after {args.num_retries} tries")
    sock.close()


if __name__ == '__main__':
    main()
