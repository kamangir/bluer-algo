from typing import Tuple, Any, Optional
import numpy as np
import cv2

from bluer_algo.tracker.classes.generic import GenericTracker
from bluer_algo.logger import logger


class KCFTracker(GenericTracker):
    algo = "kcf"

    def __init__(
        self,
        with_gui: bool = False,
    ):
        super().__init__(with_gui)

    def start(
        self,
        frame: np.ndarray,
        track_window: Tuple[int, int, int, int],
    ):
        return

    def track(
        self,
        frame: np.ndarray,
        track_window: Tuple[int, int, int, int],
        log: bool = False,
    ) -> Tuple[
        Any,  # here: always None (no extra metadata)
        Tuple[int, int, int, int],  # updated track_window (x, y, w, h)
        np.ndarray,  # full image with track_window rendered if with_gui or log
    ]:
        return None, track_window, frame
