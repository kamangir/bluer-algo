from bluer_options import string

from bluer_algo.logger import logger


class SimulatedBPSNode:
    def __init__(
        self,
        ta1: float = 30,
        ta2: float = 30,
        tr1: float = 24,
        tr2: float = 36,
    ):
        self.ta1 = ta1
        self.ta2 = ta2
        self.tr1 = tr1
        self.tr2 = tr2

    def simulate(
        self,
        length: int = 120,
    ) -> bool:
        logger.info(
            "simulating {} for {}...".format(
                self.__class__.__name__,
                string.pretty_minimal_duration(length),
            )
        )
        logger.info("🪄")
        return True
