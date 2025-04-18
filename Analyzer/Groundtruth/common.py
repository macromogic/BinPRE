from enum import Enum
from dataclasses import dataclass
from typing import Optional, List, Tuple, Dict

class SemanticType(str, Enum):
    Static = 'Static'
    Group = 'Group'
    String = 'String'
    Integer = 'Integer'
    Bytes = 'Bytes'

class SemanticFunction(str, Enum):
    Command = 'Command'
    Length = 'Length'
    Delim = 'Delim'
    CheckSum = 'CheckSum'
    Aligned = 'Aligned'
    Filename = 'Filename'


@dataclass
class Field:
    width: int
    typ: Optional[SemanticType]
    fun: Optional[SemanticFunction]

    def position(self, offset: int, width: Optional[int] = None) -> str:
        if width is None:
            width = self.width
        start_offset = offset + 1
        end_offset = offset + width
        if start_offset != end_offset:
            return f'{start_offset},{end_offset}'
        return str(start_offset)

    @classmethod
    def unknown(cls, length: int) -> 'Field':
        return cls(length, None, None)

    @classmethod
    def static(cls,
               length: int,
               fn: Optional[SemanticFunction] = None
    ) -> 'Field':
        return cls(length, SemanticType.Static, fn)

    @classmethod
    def group(cls,
              length: int,
              fn: Optional[SemanticFunction] = None
    ) -> 'Field':
        return cls(length, SemanticType.Group, fn)

    @classmethod
    def string(cls,
              length: int,
              fn: Optional[SemanticFunction] = None
    ) -> 'Field':
        return cls(length, SemanticType.String, fn)

    @classmethod
    def integer(cls,
              length: int,
              fn: Optional[SemanticFunction] = None
    ) -> 'Field':
        return cls(length, SemanticType.Integer, fn)

    @classmethod
    def bytes(cls,
              length: int,
              fn: Optional[SemanticFunction] = None
    ) -> 'Field':
        return cls(length, SemanticType.Bytes, fn)

    @classmethod
    def length(cls, length: int) -> 'Field':
        return cls(length,
                   SemanticType.Integer,
                   SemanticFunction.Length)

    @classmethod
    def delim(cls, length: int) -> 'Field':
        return cls(length,
                   SemanticType.Static,
                   SemanticFunction.Delim)

    @classmethod
    def checksum(cls, length: int) -> 'Field':
        return cls(length,
                   SemanticType.Static,
                   SemanticFunction.CheckSum)

    @classmethod
    def aligned(cls, length: int) -> 'Field':
        return cls(length,
                   SemanticType.Bytes,
                   SemanticFunction.Aligned)

    @classmethod
    def filename(cls, length: int) -> 'Field':
        return cls(length,
                   SemanticType.String,
                   SemanticFunction.Filename)

    @classmethod
    def command(cls, length: int) -> 'Field':
        return cls(length,
                   SemanticType.Static,
                   SemanticFunction.Command)


def _parse_packet_impl(
        fields: List[Field],
        last_offset: int = -1,
        vlen: Optional[List[int]] = None,
        vfields: Optional[List[List[Field]]] = None
) -> Tuple[List[int], Dict[str, str], Dict[str, str]]:
    syntax = []
    semantic = {}
    functions = {}
    vi = 0
    if vlen is None:
        vlen = []
    for field in fields:
        if field is Ellipsis:
            vfs = vfields.pop(0)
            syn, sem, fn = _parse_packet_impl(
                vfs,
                last_offset,
                vlen[vi:],
                vfields
            )
            syntax += syn
            semantic.update(sem)
            functions.update(fn)
            last_offset = syntax[-1]
        else:
            if field.width == 0:
                key = field.position(last_offset, vlen[vi])
                vi += 1
            else:
                key = field.position(last_offset)
            end_offset = int(key.split(',')[-1])
            syntax.append(end_offset)
            if field.typ:
                semantic[key] = field.typ
                if field.fun:
                    functions[key] = field.fun
            last_offset = end_offset
    return syntax, semantic, functions


class Packet:
    def __init__(self, *fields: Field):
        self.fields = fields
    
    def add_fields(self, *fields: Field):
        self.fields += fields

    def parse(self,
              vlen: Optional[List[int]] = None,
              *vfields: List[Field]
    ) -> Tuple[List[int], Dict[str, str], Dict[str, str]]:
        (
            syntax,
            semantic,
            functions
        ) = _parse_packet_impl(
            self.fields,
            vlen=vlen or [],
            vfields=list(vfields)
        )

        return [-1] + syntax, semantic, functions

    def __add__(self, other: 'Packet') -> 'Packet':
        return Packet(*self.fields, *other.fields)

    def __radd__(self, other) -> 'Packet':
        if not other:
            return self
        elif isinstance(other, Packet):
            return other.__add__(self)
        raise TypeError(f"unsupported operand type(s) for +: '{type(other)}' and 'Packet'")

def postprocess(
        gt: Dict[int, Tuple[List[int], Dict[str, str], Dict[str, str]]]
) -> Tuple[Dict[int, List[int]], Dict[int, Dict[str, str]], Dict[int, Dict[str, str]]]:
    syntax = {}
    semantic = {}
    functions = {}
    for i, (syn, sem, fn) in gt.items():
        syntax[i] = syn
        semantic[i] = sem
        functions[i] = fn
    return syntax, semantic, functions