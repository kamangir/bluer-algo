from typing import Tuple, Any
import numpy as np
import cv2

from bluer_algo.tracker.classes.generic import GenericTracker
from bluer_algo.logger import logger


class KLTTracker(GenericTracker):
    algo = "klt"

    def __init__(
        self,
        with_gui: bool = False,
    ):
        super().__init__(with_gui)

    def start(
        self,
        frame: np.ndarray,
        track_window: Tuple[int, int, int, int],
    ): ...

    def track(
        self,
        frame: np.ndarray,
        track_window: Tuple[int, int, int, int],
        log: bool = False,
    ) -> Tuple[
        Any,
        Tuple[int, int, int, int],
        np.ndarray,
    ]:
        return None, [0, 0, 0, 0], np.array([])
