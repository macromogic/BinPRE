from .common import Field, Packet, postprocess

__all__ = [
    'mirai_Syntax_Groundtruth',
    'mirai_Semantic_Groundtruth',
    'mirai_commandOffset',
    'mirai_lengthOffset',
    'mirai_Semantic_Functions_Groundtruth',
]

_mirai_empty_ids = [2, 7, 13, 17, 23, 27, 32, 37, 44, 51]

_mirai_fields = [
    [
        Field.length(2),  # Length
        Field.integer(4),  # Duration
        Field.integer(1),  # Type
        Field.length(1),  # Target count
        ...,  # Targets
        Field.length(1),  # Opt count
        ...,  # Options
    ] for _ in range(54)
]

for i in _mirai_empty_ids:
    _mirai_fields[i] = [Field.length(2)]

_mirai_target_fields = [
    Field.integer(4),  # Target IP
    Field.integer(1),  # Mask
]

_mirai_option_fields = [
    Field.integer(1),  # Option ID
    Field.length(1),  # Option length
    Field.string(0),  # Option value
]

_double_target_ids = [
    1, 3, 6, 9, 10, 12, 14, 16, 19, 21, 24, 25, 29, 31, 33, 36, 38, 40, 42, 43, 46, 48, 50, 52
]

_vlens = [
    [1],
    [1, 3],
    [],
    [2, 2],
    [3, 2],
    [],
    [1, 3],
    [],
    [3, 3],
    [1, 2],
    [2, 3],
    [],
    [3],
    [],
    [1],
    [3],
    [3],
    [],
    [],
    [1],
    [3, 1],
    [1],
    [3],
    [],
    [3],
    [2],
    [1, 3],
    [],
    [3, 1],
    [1],
    [3],
    [1, 3],
    [],
    [2],
    [3, 1],
    [],
    [3],
    [],
    [3],
    [3, 3],
    [1, 3],
    [3],
    [3],
    [4],
    [],
    [4, 2],
    [],
    [4],
    [1],
    [3, 1],
    [3],
    [],
    [2],
    [],
]

_vfields = {}
for i, v in enumerate(_vlens):
    if i in _mirai_empty_ids:
        continue
    if i in _double_target_ids:
        _vfields[i] = [_mirai_target_fields[::] * 2]
    else:
        _vfields[i] = [_mirai_target_fields[::]]
    if v:
        _vfields[i] += [_mirai_option_fields[::] * len(v)]

_mirai_gt = {
    i: Packet(*f).parse(_vlens[i], *_vfields.get(i, []))
    for i, f in enumerate(_mirai_fields)
}

(
    mirai_Syntax_Groundtruth,
    mirai_Semantic_Groundtruth,
    mirai_Semantic_Functions_Groundtruth,
) = postprocess(_mirai_gt)

mirai_lengthOffset = '0,1'
mirai_commandOffset = '6'