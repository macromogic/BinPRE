from ..common import postprocess
from .packets import EIPPayload, packet

__all__ = [
    'eip_Syntax_Groundtruth',
    'eip_Semantic_Groundtruth',
    'eip_commandOffset',
    'eip_lengthOffset',
    'eip_Semantic_Functions_Groundtruth',
]

_cip_payloads = [
    [EIPPayload.request(2)],
    [EIPPayload.request(1)],
    [EIPPayload.request(2)],
    [EIPPayload.request(25)],
    [EIPPayload.request(10)],
    [EIPPayload.request(30)],
    [EIPPayload.connection_manager()],
    [EIPPayload.request(10)],
    [EIPPayload.request(30)],
    [EIPPayload.request_path(4, 22, 22, 28, 28)],
    [EIPPayload.request_path(5, 12, 22, 22, 28, 28)],
    [EIPPayload.request_path(4, 22, 22, 28, 28)],
    [EIPPayload.request_path(3, 22, 22, 28)],
    [EIPPayload.request_path(1, 28)],
    [EIPPayload.connection_manager()],
    [EIPPayload.request(1)],
    [EIPPayload.request(1)],
    [EIPPayload.request(1)],
    [EIPPayload.request(1)],
    [EIPPayload.request(10)],
    [EIPPayload.request(30)],
    [EIPPayload.request(1)],
    [EIPPayload.request(1)],
    [EIPPayload.request(1)],
    [EIPPayload.request(1)],
    [EIPPayload.request(1)],
    [EIPPayload.request(1)],
    [EIPPayload.request(1)],
    [EIPPayload.request(25)],
    [EIPPayload.request(25)],
    [EIPPayload.request(25)],
    [EIPPayload.request(1)],
    [EIPPayload.request(1)],
    [EIPPayload.request(1)],
    [EIPPayload.request_path(5, 12, 22, 22, 28, 28)],
    [EIPPayload.request_path(4, 22, 22, 28, 28)],
    [EIPPayload.request_path(4, 22, 22, 28, 28)],
    [EIPPayload.request_path(3, 22, 22, 28)],
    [EIPPayload.request(3)],
    [EIPPayload.request(2)],
    [EIPPayload.request(2)],
    [EIPPayload.request(2)],
    [EIPPayload.request_path(1, 28)],
    [EIPPayload.request(2)],
    [EIPPayload.request(2)],
    [EIPPayload.request(2)],
    [EIPPayload.request(1)],
    [EIPPayload.request(25)],
    [EIPPayload.request(10)],
    [EIPPayload.request(30)],
]

_eip_gt = {
    i: packet(len(payloads)).parse(None, *sum(payloads, ()))
    for i, payloads in enumerate(_cip_payloads)
}

(
    eip_Syntax_Groundtruth,
    eip_Semantic_Groundtruth,
    eip_Semantic_Functions_Groundtruth
) = postprocess(_eip_gt)

eip_commandOffset = '0,1'
eip_lengthOffset = '2,3'