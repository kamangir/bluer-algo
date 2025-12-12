from typing import Tuple, Any
import numpy as np
import cv2

from bluer_algo.tracker.classes.generic import GenericTracker
from bluer_algo.logger import logger


class KCFTracker(GenericTracker):
    algo = "kcf"

    def __init__(self, with_gui: bool = False):
        super().__init__(with_gui)
        self.tracker = None
        self.is_started = False

    def start(
        self,
        frame: np.ndarray,
        track_window: Tuple[int, int, int, int],
    ):
        if frame is None or not isinstance(frame, np.ndarray):
            raise ValueError(f"{self.algo}.start: frame must be a numpy ndarray.")

        x, y, w, h = map(int, track_window)
        if w <= 0 or h <= 0:
            raise ValueError(f"{self.algo}.start: invalid track_window={track_window}.")

        self.tracker = cv2.legacy.TrackerKCF_create()
        ok = self.tracker.init(frame, (x, y, w, h))
        self.is_started = bool(ok)

        if not ok:
            logger.error(f"{self.algo}.start: init failed for bbox={track_window}.")
        else:
            logger.info(f"{self.algo}.start: initialized with bbox={track_window}.")

    def track(
        self,
        frame: np.ndarray,
        track_window: Tuple[int, int, int, int],
        log: bool = False,
    ) -> Tuple[
        Any,  # always None
        Tuple[int, int, int, int],  # updated bbox (x, y, w, h)
        np.ndarray,  # image with bbox rendered if with_gui or log
    ]:
        if frame is None or not isinstance(frame, np.ndarray):
            raise ValueError(f"{self.algo}.track: frame must be a numpy ndarray.")

        output_image = frame.copy()

        if self.tracker is None or not self.is_started:
            # Not started yet: just render the provided bbox (if asked) and return it.
            if self.with_gui or log:
                x, y, w, h = map(int, track_window)
                cv2.rectangle(output_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(
                    output_image,
                    "KCF (not started)",
                    (max(0, x), max(20, y - 8)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2,
                    cv2.LINE_AA,
                )
            logger.warning(f"{self.algo}.track: called before start().")
            return None, tuple(map(int, track_window)), output_image

        ok, bbox = self.tracker.update(frame)

        if ok:
            x, y, w, h = (int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3]))
            updated = (x, y, w, h)
            logger.info(f"{self.algo}.track: ok bbox={updated}.")
        else:
            # If update fails, keep the previous bbox (caller’s track_window)
            updated = tuple(map(int, track_window))
            logger.warning(f"{self.algo}.track: update failed; keeping bbox={updated}.")

        if self.with_gui or log:
            x, y, w, h = updated
            cv2.rectangle(output_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(
                output_image,
                "KCF",
                (max(0, x), max(20, y - 8)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2,
                cv2.LINE_AA,
            )

        return None, updated, output_image
