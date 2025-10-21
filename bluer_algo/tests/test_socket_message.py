import pytest
from typing import Dict, Any
import numpy as np

from bluer_algo.socket.message import SocketMessage


@pytest.mark.parametrize(
    ["payload"],
    [
        [{}],
        [{"this": "that"}],
        [{"image": np.zeros((480, 640, 3), np.uint8)}],
    ],
)
def test_socket_message(payload: Dict[str, Any]):
    message = SocketMessage(payload)

    assert isinstance(message, SocketMessage)
    assert isinstance(message.hostname, str)
