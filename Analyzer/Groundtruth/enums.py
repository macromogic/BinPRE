from enum import Enum

class SemanticType(str, Enum):
    Static = 'Static'
    Group = 'Group'
    String = 'String'
    BitField = 'Bit Field'
    Bytes = 'Bytes'

class SemanticFunction(str, Enum):
    Command = 'Command'
    Length = 'Length'
    Delim = 'Delim'
    CheckSum = 'CheckSum'
    Aligned = 'Aligned'
    Filename = 'Filename'