from .common import Packet, Field, postprocess

__all__ = [
    'tftp_Syntax_Groundtruth',
    'tftp_Semantic_Groundtruth',
    'tftp_commandOffset',
    'tftp_lengthOffset',
    'tftp_Semantic_Functions_Groundtruth',
]

_tftp_common_fields = [
    Field.command(2),  # opcode
    Field.filename(0),  # filename
    Field.unknown(6),  # type: octet
    Field.string(0),  # option name 1
    Field.string(0),  # option value 1
    Field.string(0),  # option name 2
    Field.string(0),  # option value 2
]

_tftp_string_fields = [
    ['pxelinux.0', 'blksize', '1432', 'tsize', '0'],
    ['ldlinux.c32', 'tsize', '0', 'blksize', '1408'],
    ['pxelinux.cfg/01-de-ad-be-ef-02-00', 'tsize', '0', 'blksize', '1408'],
    ['pxelinux.cfg/C0A80264', 'tsize', '0', 'blksize', '1408'],
    ['pxelinux.cfg/C0A8026', 'tsize', '0', 'blksize', '1408'],
    ['pxelinux.cfg/C0A802', 'tsize', '0', 'blksize', '1408'],
    ['pxelinux.cfg/C0A80', 'tsize', '0', 'blksize', '1408'],
    ['pxelinux.cfg/C0A8', 'tsize', '0', 'blksize', '1408'],
    ['pxelinux.cfg/C0A', 'tsize', '0', 'blksize', '1408'],
    ['pxelinux.cfg/C0', 'tsize', '0', 'blksize', '1408'],
    ['pxelinux.cfg/C', 'tsize', '0', 'blksize', '1408'],
    ['pxelinux.cfg/default', 'tsize', '0', 'blksize', '1408'],
    ['menu.c32', 'tsize', '0', 'blksize', '1408'],
    ['libutil.c32', 'tsize', '0', 'blksize', '1408'],
    ['pxelinux.cfg/default', 'tsize', '0', 'blksize', '1408'],
    ['memdisk', 'tsize', '0', 'blksize', '1408'],
]

_tftp_gt = {
    i: Packet(*_tftp_common_fields).parse(list(map(lambda s: len(s)+1, sf)))
    for i, sf in enumerate(_tftp_string_fields)
}

(
    tftp_Syntax_Groundtruth,
    tftp_Semantic_Groundtruth,
    tftp_Semantic_Functions_Groundtruth
) = postprocess(_tftp_gt)

tftp_commandOffset = '0,1'  # Not exist
tftp_lengthOffset = '-1'  # Not exist