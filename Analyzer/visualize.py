import argparse
import Groundtruth
from scapy.all import rdpcap
from itertools import zip_longest

FILTER_PORT = {
    'modbus': 502,
    'tftp': 69,
    'http': 80,
    'dns': 53,
    'dnp3': 20000,
    'eip': 44818,
    'mirai': 43608,
}

SEM_LABELS = {
    'Static': 'S',
    'Group': 'G',
    'String': 's',
    'Integer': 'I',
    'Bytes': 'B',
}
FN_LABELS = {
    'Command': 'C',
    'Length': 'L',
    'Delim': 'D',
    'CheckSum': 'c',
    'Aligned': 'A',
    'Filename': 'F',
}

def get_gt(protocol):
    syntax_gt = getattr(Groundtruth, f"{protocol}_Syntax_Groundtruth")
    semantic_gt = getattr(Groundtruth, f"{protocol}_Semantic_Groundtruth")
    semantic_functions_gt = getattr(Groundtruth, f"{protocol}_Semantic_Functions_Groundtruth")
    command_offset = getattr(Groundtruth, f"{protocol}_commandOffset")
    length_offset = getattr(Groundtruth, f"{protocol}_lengthOffset")
    return syntax_gt, semantic_gt, semantic_functions_gt, command_offset, length_offset


def get_pcap_data(protocol):
    pcap_path = f"pcaps/{protocol}_50.pcap"
    raw_packets = rdpcap(pcap_path)
    payloads = []
    for packet in raw_packets:
        if packet.haslayer('UDP'):
            udp_layer = packet['UDP']
            if udp_layer.dport == FILTER_PORT[protocol]:
                payloads.append(udp_layer.payload.build())
        elif packet.haslayer('TCP'):
            tcp_layer = packet['TCP']
            if tcp_layer.dport == FILTER_PORT[protocol]:
                payloads.append(tcp_layer.payload.build())
        else:
            continue
    payloads = list(filter(lambda x: x != b'', payloads))
    print(f"Loaded {len(payloads)} payloads from {pcap_path}")
    return payloads


def process_semantic(n, semantic_gt, function_gt):
    sem = {i: ['-', '-'] for i in range(n)}
    for k, v in semantic_gt.items():
        idxs = list(map(int, k.split(',')))
        for i in range(idxs[0], idxs[-1]+1):
            sem[i][0] = SEM_LABELS[v]
    for k, v in function_gt.items():
        idxs = list(map(int, k.split(',')))
        for i in range(idxs[0], idxs[-1]+1):
            sem[i][1] = FN_LABELS[v]
    return {k: ''.join(v) for k, v in sem.items()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('protocol', type=str, choices=['tftp', 'http', 'dns', 'dnp3', 'eip', 'mirai'])
    args = parser.parse_args()
    (
        syntax_gt,
        semantic_gt,
        semantic_functions_gt,
        command_offset,
        length_offset,
    ) = get_gt(args.protocol)
    payloads = get_pcap_data(args.protocol)
    print(f"=== Protocol {args.protocol}: Command Offset: {command_offset}, Length Offset: {length_offset} ===")
    for i, payload in enumerate(payloads):
        print(f"+++ Payload #{i} +++")
        n = len(payload)
        syn = syntax_gt[i][::]
        print(f"Syntax GT: {syn}, Length: {len(payload)}")
        assert syn[0] == -1, "First element of syntax_gt should be -1"
        assert syn[-1]+1 == len(payload), f"Length mismatch in syntax_gt: {syn[-1]+1} != {len(payload)}"
        sem = process_semantic(n, semantic_gt[i], semantic_functions_gt[i])


        bi = syn.pop(0)
        for j in range(0, n, 16):
            s = payload[j:j+16]
            m = len(s)
            # hexa = ' ' + ' '.join([f"{c:02x}" for c in s]) + ' '
            # sema = ' ' + ' '.join([f"{sem[j+k]}" for k in range(m)]) + ' '
            # text = ''.join([chr(c) if 32 <= c < 127 else '.' for c in s])
            boundary = [' ' for _ in range(m)]
            while bi < j+m:
                if bi >= 0:
                    boundary[bi-j] = '|'
                if not syn:
                    bi = -1
                    break
                bi = syn.pop(0)
            hexa = [f"{c:02x}" for c in s]
            sema = [f"{sem[j+k]}" for k in range(m)]
            hexa = "".join((a or "") + (b or "") for a, b in zip(hexa, boundary))
            sema = "".join((a or "") + (b or "") for a, b in zip(sema, boundary))
            text = ''.join([chr(c) if 32 <= c < 127 else '.' for c in s])
            print(f"{hexa:<50} {text}")
            print(f"{sema:<50}")
        print()


if __name__ == "__main__":
    main()
