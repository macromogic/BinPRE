from ..common import Field, Packet
from . import srvsvc
from enum import Enum

__all__ = [
    'smb2_Syntax_Groundtruth',
    'smb2_Semantic_Groundtruth',
    'smb2_commandOffset',
    'smb2_lengthOffset',
    'smb2_Semantic_Functions_Groundtruth',
]

class _Cmd(Enum):
    NEGOTIATE = 0x00
    SESSION_SETUP = 0x01
    LOGOFF = 0x02
    TREE_CONNECT = 0x03
    TREE_DISCONNECT = 0x04
    CREATE = 0x05
    CLOSE = 0x06
    FLUSH = 0x07
    READ = 0x08
    WRITE = 0x09
    LOCK = 0x0A
    IOCTL = 0x0B
    CANCEL = 0x0C
    ECHO = 0x0D
    FIND = 0x0E
    NOTIFY = 0x0F
    GET_INFO = 0x10
    SET_INFO = 0x11
    OPLOCK_BREAK = 0x12
    S2C_NOTIFY = 0x13

_smb2_common_headers = [
    Field.integer(1),  # NetBIOS Message Type
    Field.length(3),  # NetBIOS Length
    Field.static(4),  # Protocol ID
    Field.length(2),  # SMB2 Header Length
    Field.integer(2),  # Credit Charge
    Field.integer(2),  # Channel Sequence
    Field.static(2),  # Reserved
    Field.command(2),  # Command
    Field.integer(2),  # Credit Request
    Field.integer(4),  # Flags
    Field.integer(4),  # Chain Offset
    Field.integer(8),  # Message ID
    Field.static(4),  # Reserved
    Field.integer(4),  # Tree ID
    Field.integer(8),  # Session ID
    Field.bytes(16),  # Signature
]

_smb2_cmd_fields = {
    _Cmd.TREE_CONNECT: [
        Field.length(2),  # Structure Size
        Field.integer(2),  # Flags
        Field.integer(2),  # Blob Offset
        Field.integer(2),  # Blob Length
        Field.string(0), # Path
    ],
    _Cmd.CREATE: [
        Field.length(2),  # Structure Size
        Field.aligned(1),  # Padding
        Field.integer(1),  # Oplock
        Field.integer(4),  # Impersonation Level
        Field.integer(8),  # Create Flags
        Field.static(8),  # Reserved
        Field.integer(4),  # Access Mask
        Field.integer(4),  # File Attributes
        Field.integer(4),  # Share Access
        Field.integer(4),  # Create Disposition
        Field.integer(4),  # Create Options
        Field.integer(2),  # Name Offset
        Field.length(2),  # Name Length
        Field.integer(4),  # Create Contexts Offset
        Field.length(4),  # Create Contexts Length
        ...  # Name Or Additional Info
    ],
    _Cmd.GET_INFO: [
        Field.length(2),  # Structure Size
        Field.integer(1),  # Class
        Field.integer(1),  # Info Level
        Field.integer(4),  # Max Resp Size
        Field.integer(4),  # Input Buffer Offset
        Field.static(4),  # Reserved
        Field.integer(4),  # Input Buffer Length
        Field.integer(4),  # Additional Info
        Field.integer(4),  # Flags
        Field.integer(16),  # File ID
    ],
    _Cmd.WRITE: [
        Field.length(2),  # Structure Size
        Field.integer(2),  # Data Offset
        Field.length(4),  # Length
        Field.integer(8),  # Offset
        Field.integer(16),  # File ID
        Field.integer(4),  # Channel
        Field.integer(4),  # Remaining
        Field.integer(2),  # Write Channel Info Offset
        Field.length(2),  # Write Channel Info Length
        Field.integer(4),  # Write Flags
        ### DCERPC Payload ###
        Field.static(1),  # Major Version
        Field.static(1),  # Minor Version
        Field.integer(1),  # Packet Type
        Field.integer(1),  # Packet Flags
        Field.integer(4),  # Data Representation
        Field.integer(2),  # Frag Length
        Field.integer(2),  # Auth Length
        Field.integer(4),  # Call ID
        Field.integer(2),  # Max Xmit Frag
        Field.integer(2),  # Max Recv Frag
        Field.integer(4),  # Assoc Group
        Field.integer(4),  # Num Context Items (=2)
        ### Context Item 1 ###
        Field.integer(2),  # Context ID
        Field.integer(2),  # Num Trans Items (=1)
        Field.integer(16),  # Interface UUID
        Field.integer(2),  # Interface Major Version
        Field.integer(2),  # Interface Minor Version
        Field.integer(16),  # Transfer Syntax UUID
        Field.integer(4),  # Transfer Syntax Version
        ### Context Item 2 ###
        Field.integer(2),  # Context ID
        Field.integer(2),  # Num Trans Items (=1)
        Field.integer(16),  # Interface UUID
        Field.integer(2),  # Interface Major Version
        Field.integer(2),  # Interface Minor Version
        Field.integer(16),  # Transfer Syntax UUID
        Field.integer(4),  # Transfer Syntax Version
    ],
    _Cmd.READ: [
        Field.length(2),  # Structure Size
        Field.integer(1),  # Padding
        Field.integer(1),  # Flags
        Field.length(4),  # Length
        Field.integer(8),  # Offset
        Field.integer(16),  # File ID
        Field.integer(4),  # Minimum Count
        Field.integer(4),  # Channel
        Field.integer(4),  # Remaining
        Field.integer(2),  # Read Channel Info Offset
        Field.length(2),  # Read Channel Info Length
        Field.delim(1),
    ],
    _Cmd.IOCTL: [
        Field.length(2),  # Structure Size
        Field.static(2),  # Reserved
        Field.command(4),  # Ctl Code
        Field.integer(16),  # File ID
        Field.integer(4),  # Input Offset
        Field.length(4),  # Input Length
        Field.integer(4),  # Max Ioctl In Size
        Field.integer(4),  # Output Offset
        Field.length(4),  # Output Length
        Field.integer(4),  # Max Ioctl Out Size
        Field.integer(4),  # Flags
        Field.static(4),  # Reserved
        ...  # Payload
    ],
    _Cmd.CLOSE: [
        Field.length(2),  # Structure Size
        Field.integer(2),  # Flags
        Field.aligned(4),
        Field.integer(16),  # File ID
    ],
    _Cmd.NOTIFY: [
        Field.length(2),  # Structure Size
        Field.integer(2),  # Notify Flags
        Field.integer(4),  # Output Buffer Length
        Field.integer(16),  # File ID
        Field.integer(4),  # Completion Filter
        Field.integer(4),  # Reserved
    ],
    _Cmd.FIND: [
        Field.length(2),  # Structure Size
        Field.integer(1),  # Info Level
        Field.integer(1),  # Flags
        Field.integer(4),  # File Index
        Field.integer(16),  # File ID
        Field.integer(2),  # Pattern Offset
        Field.length(2),  # Pattern Length
        Field.length(4),  # Output Buffer Length
        Field.string(0),  # Pattern
    ],
    _Cmd.CANCEL: [
        Field.length(2),  # Structure Size
        Field.unknown(2),
    ],
}

_cmds = [
    _Cmd.TREE_CONNECT,
    _Cmd.CREATE,
    _Cmd.GET_INFO,
    _Cmd.WRITE,
    _Cmd.READ,
    _Cmd.IOCTL,
    _Cmd.CLOSE,
    _Cmd.IOCTL,
    _Cmd.TREE_CONNECT,
    _Cmd.CREATE,
    _Cmd.GET_INFO,
    _Cmd.CREATE,
    _Cmd.GET_INFO,
    _Cmd.WRITE,
    _Cmd.READ,
    _Cmd.IOCTL,
    _Cmd.CLOSE,
    _Cmd.CREATE,
    _Cmd.CREATE,
    _Cmd.CREATE,
    _Cmd.FIND,
    _Cmd.CREATE,
    _Cmd.READ,
    _Cmd.CLOSE,
    _Cmd.GET_INFO,
    _Cmd.GET_INFO,
    _Cmd.IOCTL,
    _Cmd.CREATE,
    _Cmd.GET_INFO,
    _Cmd.GET_INFO,
    _Cmd.CLOSE,
    _Cmd.CANCEL,
    _Cmd.CREATE,
    _Cmd.CLOSE,
    _Cmd.CREATE,
    _Cmd.CLOSE,
    _Cmd.CREATE,
    _Cmd.CLOSE,
    _Cmd.CREATE,
    _Cmd.CLOSE,
    _Cmd.NOTIFY,
    _Cmd.CANCEL,
    _Cmd.CREATE,
    _Cmd.CREATE,
    _Cmd.CLOSE,
    _Cmd.CREATE,
    _Cmd.CLOSE,
    _Cmd.CREATE,
]

_smb2_packets = {
    i: Packet(*_smb2_common_headers, *_smb2_cmd_fields[c])
    for i, c in enumerate(_cmds)
}

_smb2_packets[10].add_fields(
    Field.unknown(8),
    *_smb2_common_headers,
    *_smb2_cmd_fields[_Cmd.GET_INFO],
)

_smb2_packets[17].add_fields(
    *_smb2_common_headers,
    *_smb2_cmd_fields[_Cmd.NOTIFY],
)


_smb2_packets[20].add_fields(
    Field.unknown(8),
    *_smb2_common_headers,
    *_smb2_cmd_fields[_Cmd.FIND],
)

_smb2_packets[28].add_fields(
    Field.unknown(8),
    *_smb2_common_headers,
    *_smb2_cmd_fields[_Cmd.GET_INFO],
)

_create_common_fields = [
    Field.integer(4),  # Chain Offset
    Field.integer(2),  # Tag Offset
    Field.integer(4),  # Tag Length
    Field.integer(2),  # Data Offset
    Field.integer(4),  # Data Length
    Field.command(4),  # Tag
    Field.unknown(4),
]

_ioctl_payloads = {
    5: srvsvc.srvsvc_netshareenumall_payload,
    7: [Field.integer(2), Field.string(0)],
    15: srvsvc.srvsvc_netsharegetinfo_payload,
    26: [Field.unknown(14), Field.string(0)],
}

_create_payloads = {
    1: [
        Field.string(0)
    ],
    9: [
        Field.unknown(8),
        *_create_common_fields,
        Field.integer(16),
        *_create_common_fields,
        *_create_common_fields,
    ],
    11: [
        Field.string(0)
    ],
    17: [
        Field.unknown(8),
        *_create_common_fields,
        Field.integer(16),
        *_create_common_fields,
        *_create_common_fields,
    ],
    18: [
        Field.string(0),
        Field.delim(2),
        *_create_common_fields,
        Field.integer(16),
        *_create_common_fields,
        *_create_common_fields,
    ],
    19: [
        Field.unknown(8),
        *_create_common_fields,
        Field.integer(16),
        *_create_common_fields,
    ],
    21: [
        Field.string(0),
        Field.delim(2),
        *_create_common_fields,
        Field.integer(16),
        *_create_common_fields,
        *_create_common_fields,
    ],
    27: [
        Field.unknown(8),
        *_create_common_fields,
        Field.integer(16),
        *_create_common_fields,
    ],
    32: [
        Field.string(0),
        Field.delim(2),
        Field.unknown(4),
        *_create_common_fields,
        Field.integer(16),
        *_create_common_fields,
        Field.integer(16),
        *_create_common_fields,
        *_create_common_fields,
    ],
    34: [
        Field.string(0),
        Field.delim(2),
        Field.unknown(4),
        *_create_common_fields,
        Field.integer(16),
        *_create_common_fields,
        *_create_common_fields,
    ],
    36: [
        Field.unknown(8),
        *_create_common_fields,
        Field.integer(16),
        *_create_common_fields,
        *_create_common_fields,
    ],
    38: [
        Field.unknown(8),
        *_create_common_fields,
        Field.integer(16),
        *_create_common_fields,
        *_create_common_fields,
    ],
    42: [
        Field.string(0),
        Field.delim(2),
        Field.unknown(4),
        *_create_common_fields,
        Field.integer(16),
        *_create_common_fields,
        Field.integer(16),
        *_create_common_fields,
        *_create_common_fields,
    ],
    43: [
        Field.unknown(8),
        *_create_common_fields,
        Field.integer(16),
        *_create_common_fields,
        *_create_common_fields,
    ],
    45: [
        Field.unknown(8),
        *_create_common_fields,
        Field.integer(16),
        *_create_common_fields,
    ],
    47: [
        Field.string(0),
        Field.delim(2),
        Field.unknown(4),
        *_create_common_fields,
        Field.integer(16),
        *_create_common_fields,
        *_create_common_fields,
    ],
}

_vfields = {**_ioctl_payloads, **_create_payloads}

_vlens = {
    0: [34],
    1: [12],
    5: [26],
    7: [48],
    8: [48],
    11: [12],
    15: [22, 24],
    18: [22],
    20: [2],
    21: [46],
    26: [16],
    32: [10],
    34: [10],
    42: [10],
    47: [10],
}

_smb2_gt = {
    i: p.parse(_vlens.get(i), _vfields.get(i, []))
    for i, p in _smb2_packets.items()
}

smb2_Syntax_Groundtruth = {
    i: gt[0] for i, gt in _smb2_gt.items()
}

smb2_Semantic_Groundtruth = {
    i: gt[1] for i, gt in _smb2_gt.items()
}

smb2_Semantic_Functions_Groundtruth = {
    i: gt[2] for i, gt in _smb2_gt.items() if gt[2]
}

smb2_commandOffset = '16,17'
smb2_lengthOffset = '1,3'