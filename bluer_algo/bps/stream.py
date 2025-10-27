from typing import List

from bluer_objects import file, objects
from bluer_objects.metadata import get_from_object, post_to_object

from bluer_algo.bps.ping import Ping
from bluer_algo.logger import logger


class Stream:
    def __init__(self):
        self.ping: Ping = Ping(log=False)
        self.history: List[Ping] = []

    def append(
        self,
        ping: Ping,
        log: bool = False,
    ) -> bool:
        if ping.id in [ping.id for ping in self.history]:
            if log:
                logger.info(f"repeat ping ignored: {ping.as_str()}")

            return False

        self.history.append(ping)
        if log:
            logger.info(f"🏓 # unique pings: {len(self.history)}")

        return True

    def generate(
        self,
        simulate: bool = False,
        as_dict: dict = {},
    ):
        if simulate:
            logger.info("simulating stream...")
            self.ping = Ping.simulate()
        else:
            logger.info("generating stream...")
            self.ping = Ping(as_dict)

    @classmethod
    def load(cls, object_name: str) -> "Stream":
        _, stream = file.load(
            objects.path_of(
                object_name=object_name,
                filename="bps-stream.dill",
            ),
            default=Stream(),
            ignore_error=True,
        )
        assert isinstance(stream, Stream)

        logger.info(f"loaded {len(stream.history)} ping(s)")

        return stream

    def save(
        self,
        object_name: str,
        log: bool = True,
    ) -> bool:
        if not post_to_object(
            object_name,
            "bps",
            {
                "ping": self.ping.as_dict(),
                "history": [ping.as_dict() for ping in self.history],
            },
        ):
            return False

        return file.save(
            objects.path_of(
                object_name=object_name,
                filename="bps-stream.dill",
            ),
            self,
            log=log,
        )
