from typing import Any, Type

from blueness import module

from bluer_algo import NAME
from bluer_algo.socket.connection import SocketConnection
from bluer_algo.logger import logger

NAME = module.name(__file__, NAME)


def test_receiving(expected_class: Type = str) -> bool:
    logger.info(f"{NAME}: testing receiving ...")

    socket = SocketConnection.listen_on()

    success, data = socket.receive_data(expected_class)
    if not success:
        return success

    logger.info(f"received {data}")
    print(data)
    return True


def test_sending(
    target_host: str,
    data: Any = "hello-world",
) -> bool:
    logger.info(f"{NAME}: testing sending ...")

    socket = SocketConnection.connect_to(target_host)

    return socket.send_data(data)
