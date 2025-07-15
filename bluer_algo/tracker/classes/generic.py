import numpy as np

from bluer_algo.logger import logger


class GenericTracker:
    def __init__(self):
        logger.info(f"{self.__class__.__name__} initialized.")

    def start(frame: np.ndarray): ...
