from bluer_options import string

from bluer_algo.bps.simulation.timing.specs import Specs
from bluer_algo.logger import logger


class Node:
    def __init__(
        self,
        specs: Specs = Specs(),
    ):
        self.specs = specs

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
