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

    def position(self, offset: int) -> str:
        start_offset = offset + 1
        end_offset = offset + self.width
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


def __parse_packet_impl(
        fields: List[Field],
        last_offset: int = -1,
        vlen: Optional[List[int]] = None,
        vfields: Optional[List[List[Field]]] = None
) -> Tuple[List[int], Dict[str, str], Dict[str, str]]:
    syntax = []
    semantic = {}
    functions = {}
    vi = 0
    for field in fields:
        if field is Ellipsis:
            vfs = vfields[0]
            syn, sem, fn = __parse_packet_impl(
                vfs,
                last_offset,
                vlen[vi:],
                vfields[1:]
            )
            syntax += syn
            semantic.update(sem)
            functions.update(fn)
        else:
            if field.width == 0:
                field.width = vlen[vi]
                vi += 1

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
        ) = __parse_packet_impl(
            self.fields,
            vlen=vlen,
            vfields=vfields
        )

        return [-1] + syntax, semantic, functions
