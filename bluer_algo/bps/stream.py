from typing import List, Tuple

from bluer_objects import file, objects

from bluer_algo.bps.ping import Ping
from bluer_algo.logger import logger


class Stream:
    def __init__(self):
        self.ping: Ping = Ping()
        self.history: List[Ping] = []

    def filename(self, object_name: str) -> str:
        return objects.path_of(
            object_name=object_name,
            filename="bps.yaml",
        )

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

        _, metadata = file.load_yaml(
            stream.filename(object_name),
            ignore_error=True,
        )

        assert isinstance(metadata, dict)

        stream.ping = Ping(metadata.get("ping", Ping().as_dict()))
        stream.history = [Ping(ping) for ping in metadata.get("history", [])]

        return stream

    def save(
        self,
        object_name: str,
        log: bool = True,
    ) -> bool:
        return file.save_yaml(
            self.filename(object_name),
            {
                "ping": self.ping.as_dict(),
                "history": [ping.as_dict() for ping in self.history],
            },
            log=log,
        )
