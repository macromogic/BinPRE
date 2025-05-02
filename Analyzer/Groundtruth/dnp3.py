from .common import Field, Packet, postprocess

__all__ = [
    'dnp3_Syntax_Groundtruth',
    'dnp3_Semantic_Groundtruth',
    'dnp3_commandOffset',
    'dnp3_lengthOffset',
    'dnp3_Semantic_Functions_Groundtruth',
]

_dnp3_common_fields = [
    ### Link Header ###
    Field.static(2),  # Start bytes
    Field.length(1),  # Length
    Field.unknown(1),  # Control
    Field.integer(2),  # Destination
    Field.integer(2),  # Source
    Field.checksum(2),  # Data link header checksum
    ### Transport Header ###
    Field.unknown(1),  # Transport control
    ### Application Header ###
    Field.unknown(1),  # Application control
    Field.command(1),  # Function code
    ### Application Data ###
    ...,
    Field.checksum(2),  # Application data checksum
]

_dnp3_payload_fields = [
    Field.unknown(2),  # Object type
    Field.integer(1),  # Qualifier
]

_dnp3_n_packets = 53

_dnp3_number_payloads = {
    i: 1 for i in range(_dnp3_n_packets)
}
_dnp3_number_payloads.update({
    i: 0 for i in [1, 10, 24, 39]
})
_dnp3_number_payloads.update({
    i: 3 for i in [2, 11, 25, 40]
})
_dnp3_number_payloads.update({
    i: 4 for i in [0, 3, 9, 12, 23, 26, 38, 41]
})

_dnp3_gt = {
    i: Packet(*_dnp3_common_fields).parse(None, _dnp3_payload_fields * n)
    for i, n in _dnp3_number_payloads.items()
}

(
    dnp3_Syntax_Groundtruth,
    dnp3_Semantic_Groundtruth,
    dnp3_Semantic_Functions_Groundtruth
) = postprocess(_dnp3_gt)
dnp3_commandOffset = '12'
dnp3_lengthOffset = '2'