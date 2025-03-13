from ..common import Field

srvsvc_header = [
    Field.static(1),  # Major Version
    Field.static(1),  # Minor Version
    Field.integer(1),  # Packet Type
    Field.integer(1),  # Packet Flags
    Field.integer(4),  # Data Representation
    Field.integer(2),  # Frag Length
    Field.integer(2),  # Auth Length
    Field.integer(4),  # Call ID
    Field.integer(4),  # Alloc Hint
    Field.integer(2),  # Context ID
    Field.command(2),  # Opnum
    # Payload
]

srvsvc_netshareenumall_payload = srvsvc_header + [
    Field.integer(4),  # Referent ID
    Field.integer(4),  # Max Count
    Field.integer(4),  # Offset
    Field.length(4),  # Actual Count
    Field.string(0),  # Path
    Field.delim(2),
    Field.integer(4),  # Level
    Field.integer(4),  # Count???
    Field.integer(4),  # Referent ID
    Field.integer(4),  # Count
    Field.delim(4),  # Null Pointer
    Field.integer(4),  # Max Buffer
    Field.delim(4),  # Null Pointer
]

srvsvc_netsharegetinfo_payload = srvsvc_header + [
    Field.integer(4),  # Referent ID
    Field.integer(4),  # Max Count
    Field.integer(4),  # Offset
    Field.length(4),  # Actual Count
    Field.string(0),  # Path
    Field.delim(2),
    Field.integer(4),  # Max Count
    Field.integer(4),  # Offset
    Field.length(4),  # Actual Count
    Field.string(0),  # Path
    Field.integer(4),  # Level
]