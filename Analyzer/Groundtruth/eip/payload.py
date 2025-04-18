from ..common import Field
from enum import Enum
from typing import List

_cip_request_common_fields = [
    Field.integer(1),  # Service Code
    Field.length(1),  # Request Path Size
    Field.integer(1),  # Request Path #1 Flag
    Field.integer(1),  # Request Path #1 Class
    Field.integer(1),  # Request Path #2 Flag
    Field.integer(1),  # Request Path #2 Instance
    Field.integer(2),  # Number of Services
]

_cip_offset_field = [Field.integer(2)]

_cip_service_fields_4c = [
    Field.integer(1),  # Service Code
    Field.length(1),  # Request Path Size
    Field.integer(1),  # Request Path #1 Flag
    Field.integer(1),  # Request Path #1 Class
    Field.integer(1),  # Request Path #2 Flag
    Field.integer(1),  # Request Path #2 Instance
    Field.bytes(6),  # Command Specific Data
]

_cip_service_fields_4e = [
    Field.integer(1),  # Service Code
    Field.length(1),  # Request Pathyy Size
    Field.integer(1),  # Request Path Flag
    Field.length(1),  # Request Path Length
    Field.string(0),  # Request Path
    Field.bytes(4),  # Command Specific Data
]

_cip_cm_fields = [
    Field.integer(1),  # Service Code
    Field.unknown(5),
    Field.integer(1),  # Tick Flags
    Field.integer(1),  # Tick Count
    Field.length(2),  # Embedded Message Request Size
    Field.integer(1),  # Service Flag
    Field.length(1),  # Request Path Size
    Field.integer(1),  # Request Path #1 Flag
    Field.integer(1),  # Request Path #1 Class
    Field.integer(1),  # Request Path #2 Flag
    Field.integer(1),  # Request Path #2 Instance
    Field.bytes(2),  # Command Specific Data
    Field.length(1),  # Route Path Size
    Field.static(1),  # Reserved
    Field.integer(1),  # Route Path Flags
    Field.integer(1),  # Route Link Address
]

class EIPItem(Enum):
    NULL = 0x0000
    CONNECTED_ADDR = 0x00a1
    CONNECTED_DATA = 0x00b1
    UNCONNECTED_DATA = 0x00b2

    def to_fields(self) -> List[Field]:
        match self:
            case self.NULL:
                return [Field.integer(2), Field.integer(2)]
            case self.CONNECTED_ADDR:
                return [Field.integer(2), Field.integer(2), Field.integer(4)]
            case self.CONNECTED_DATA:
                return [Field.integer(2), Field.integer(2), Field.integer(2)]
            case self.UNCONNECTED_DATA:
                return [Field.integer(2), Field.integer(2)]
            case _:
                raise ValueError(f"Unknown item: {item}")

class CIPItem:
    @classmethod
    def request(cls, n: int) -> List[Field]:
        return _cip_request_common_fields + _cip_offset_field * n + _cip_service_fields_4c * n

    @classmethod
    def request_path(cls, n: int, *length: int) -> List[Field]:
        offset_fields = _cip_offset_field * n
        service_fields = []
        for i in range(n):
            fields = _cip_service_fields_4e.copy()
            fields[-2] = Field.string(length[i])
            service_fields.extend(fields)
        return _cip_request_common_fields + offset_fields + service_fields

    @classmethod
    def connection_manager(cls) -> List[Field]:
        return _cip_cm_fields