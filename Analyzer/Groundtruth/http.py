from .common import Field, Packet, postprocess
from scapy.all import rdpcap
from pathlib import Path

__all__ = [
    'http_Syntax_Groundtruth',
    'http_Semantic_Groundtruth',
    'http_commandOffset',
    'http_lengthOffset',
    'http_Semantic_Functions_Groundtruth',
]

_binpre_path = Path(__file__).resolve().parent.parent.parent
_http_pcap_path = _binpre_path / 'Analyzer' / 'pcaps' / 'http_50.pcap'
_packets = rdpcap(str(_http_pcap_path))
_http_gt = {}
_i = 0
for _pkt in _packets:
    if _pkt.haslayer('TCP') and _pkt['TCP'].dport == 80:
        if _payload := _pkt['TCP'].payload.build():
            _raw_fields = _payload.strip().split(b'\r\n')
            _fields = [Field.string(len(f)+2) for f in _raw_fields] + [Field.delim(2)]
            _http_gt[_i] = Packet(*_fields).parse()
            _i += 1

print(len(_http_gt))

(
    http_Syntax_Groundtruth,
    http_Semantic_Groundtruth,
    http_Semantic_Functions_Groundtruth
) = postprocess(_http_gt)

http_commandOffset = '-1'  # Not exist
http_lengthOffset = '-1'  # Not exist