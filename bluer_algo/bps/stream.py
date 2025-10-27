from typing import List

from bluer_objects import file
from bluer_objects.metadata import get_from_object, post_to_object

from bluer_algo.bps.ping import Ping
from bluer_algo.logger import logger


class Stream:
    def __init__(self):
        self.ping: Ping = Ping(log=False)
        self.history: List[Ping] = []

    @classmethod
    def generate(
        cls,
        simulate: bool = False,
        as_dict: dict = {},
    ) -> "Stream":
        stream = cls()

        if simulate:
            logger.info("simulating stream...")
            stream.ping = Ping.simulate()
        else:
            logger.info("generating stream...")
            stream.ping = Ping(as_dict)

        return stream

    @classmethod
    def load(cls, object_name: str) -> "Stream":
        stream = cls()

        logger.info(f"loading stream from {object_name}...")

        metadata = get_from_object(object_name, "bps", {})
        assert isinstance(metadata, dict)

        stream.ping = Ping(metadata.get("ping", Ping().as_dict()))
        stream.history = [Ping(ping) for ping in metadata.get("history", [])]

        return stream

    def save(
        self,
        object_name: str,
        log: bool = True,
    ) -> bool:
        return post_to_object(
            object_name,
            "bps",
            {
                "ping": self.ping.as_dict(),
                "history": [ping.as_dict() for ping in self.history],
            },
        )
