from .common import SemanticType, SemanticFunction

__all__ = [
    'cip_Syntax_Groundtruth',
    'cip_Semantic_Groundtruth',
    'cip_commandOffset',
    'cip_lengthOffset',
    'cip_Semantic_Functions_Groundtruth',
]

_syntax_groundtruth = [
    -1, 0, 1, 3, 5, 7, 8, 9, 11, 15,
]

_semantic_groundtruth = {
    '0': SemanticType.Integer, # [7:4] Version; [3:0] Header length
    '1': SemanticType.Integer, # Service
    '2,3': SemanticType.Integer, # Total length
    '4,5': SemanticType.Static, # Identification
    '6,7': SemanticType.Integer, # [15:13] Flags; [12:0] Fragment offset
    '8': SemanticType.Integer, # TTL
    '9': SemanticType.Static, # Protocol
    '10,11': SemanticType.Integer, # Header checksum
    '12,15': SemanticType.Bytes, # Source IP
    '16,19': SemanticType.Bytes, # Destination IP
}

_semantic_functions_groundtruth = {
    '2,3': SemanticFunction.Length,
    '10,11': SemanticFunction.CheckSum,
}

cip_Syntax_Groundtruth = {
    i: _syntax_groundtruth
    for i in range(50)
}

cip_Semantic_Groundtruth = {
    i: _semantic_groundtruth
    for i in range(50)
}

cip_Semantic_Functions_Groundtruth = {
    i: _semantic_functions_groundtruth
    for i in range(50)
}

cip_commandOffset = '1'
cip_lengthOffset = '2,3'