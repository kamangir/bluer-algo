import random
from typing import Dict

from bluer_options import string

from bluer_algo.logger import logger


class Ping:
    def __init__(
        self,
        as_dict: Dict[str, float] = {},
        log: bool = True,
    ):
        self.id = as_dict.get(
            "id", string.timestamp(unique_length=6)
        )  # limited by advertisement packet size limits - can use 7.

        self.x = as_dict.get("x", 0.0)
        self.y = as_dict.get("y", 0.0)
        self.z = as_dict.get("z", 0.0)
        self.sigma = as_dict.get("sigma", 1000.0)
        self.tx_power = as_dict.get("tx_power", -1)  # -1: unknown
        self.rssi = as_dict.get("rssi", -1)  # -1: unknown

        if log:
            logger.info(self.as_str())

    def as_dict(self) -> dict:
        return {
            "id": self.id,
            "x": self.x,
            "y": self.y,
            "z": self.z,
            "sigma": self.sigma,
            "tx_power": self.tx_power,
            "rssi": self.rssi,
        }

    def as_str(self) -> str:
        return "{}[{}] @ [{:.2f} {:.2f} {:.2f}] +- {:.2f} m - tx-power: {:.2f} dBm, rssi: {:.2f} dBm".format(
            self.__class__.__name__,
            self.id,
            self.x,
            self.y,
            self.z,
            self.sigma,
            self.tx_power,
            self.rssi,
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
