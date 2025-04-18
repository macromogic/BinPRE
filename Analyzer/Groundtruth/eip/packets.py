from ..common import Packet, Field
from .payload import EIPItem, CIPItem
from typing import Tuple, List

_eip_common_fields = [
    ### Encapsulation Header ###
    Field.command(2),  # Command
    Field.length(2),  # Length
    Field.integer(4),  # Session Handle
    Field.integer(4),  # Status
    Field.integer(8),  # Sender Context
    Field.integer(4),  # Options
    ### Command Specific Data ###
    Field.integer(4),  # Interface Handle
    Field.integer(2),  # Timeout
    Field.integer(2),  # Item Count
    ...,  # Item Data 1
    ...,  # Item Data 2
    ### CIP ###
    ...,  # Service Packets
]

def packet(n: int) -> Packet:
    return sum([Packet(*_eip_common_fields)] * n)

class EIPPayload:
    @classmethod
    def request(cls, n: int) -> Tuple[List[Field], List[Field], List[Field]]:
        return (
            EIPItem.CONNECTED_ADDR.to_fields(),
            EIPItem.CONNECTED_DATA.to_fields(),
            CIPItem.request(n),
        )

    @classmethod
    def request_path(cls, n: int, *lengths: int) -> Tuple[List[Field], List[Field], List[Field]]:
        return (
            EIPItem.CONNECTED_ADDR.to_fields(),
            EIPItem.CONNECTED_DATA.to_fields(),
            CIPItem.request_path(n, *lengths),
        )

    @classmethod
    def connection_manager(cls) -> Tuple[List[Field], List[Field], List[Field]]:
        return (
            EIPItem.NULL.to_fields(),
            EIPItem.UNCONNECTED_DATA.to_fields(),
            CIPItem.connection_manager(),
        )
