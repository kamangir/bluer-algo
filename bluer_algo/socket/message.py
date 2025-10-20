from typing import Dict, Any

from bluer_options.env import abcli_hostname


class SocketMessage:
    def __init__(
        self,
        payload: Dict[str, Any] = {},
    ):
        self.payload: Dict[str, Any] = payload.copy()

        self.hostname = abcli_hostname
