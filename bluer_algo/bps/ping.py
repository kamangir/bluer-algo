import random
from typing import Dict

from bluer_algo.logger import logger


class Ping:
    def __init__(
        self,
        as_dict: Dict[str, float] = {},
        log: bool = True,
    ):
        self.x = as_dict.get("x", 0.0)
        self.y = as_dict.get("y", 0.0)
        self.z = as_dict.get("z", 0.0)
        self.sigma = as_dict.get("sigma", 1000.0)

        if log:
            logger.info(self.as_str())

    def as_dict(self) -> dict:
        return {
            "x": self.x,
            "y": self.y,
            "z": self.z,
            "sigma": self.sigma,
        }

    def as_str(self) -> str:
        return "{}@[{:.2f},{:.2f},{:.2f}]+-{:.2f} m".format(
            self.__class__.__name__,
            self.x,
            self.y,
            self.z,
            self.sigma,
        )

    @classmethod
    def simulate(
        cls,
        min: float = 0.0,
        max: float = 100.0,
        log: bool = True,
    ) -> "Ping":
        return cls(
            {
                "x": random.uniform(min, max),
                "y": random.uniform(min, max),
                "z": random.uniform(min, max),
                "sigma": random.uniform(min, max),
            },
            log=log,
        )
