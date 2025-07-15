import numpy as np
import cv2 as cv
import argparse

from bluer_algo.logger import logger

parser = argparse.ArgumentParser(
    description="This sample demonstrates the meanshift algorithm. \
                                              The example file can be downloaded from: \
                                              https://www.bogotobogo.com/python/OpenCV_Python/images/mean_shift_tracking/slow_traffic_small.mp4"
)
parser.add_argument(
    "--filename",
    type=str,
    help="path to video file.",
)
parser.add_argument(
    "--frame_count",
    type=int,
    default=-1,
    help="-1: all",
)
parser.add_argument(
    "--log",
    type=int,
    default=0,
    help="0 | 1",
)
parser.add_argument(
    "--show_gui",
    type=int,
    default=1,
    help="0 | 1",
)
args = parser.parse_args()

cap = cv.VideoCapture(args.filename)

# take first frame of the video
ret, frame = cap.read()

# setup initial location of window
x, y, w, h = 300, 200, 100, 50  # simply hardcoded the values
track_window = (x, y, w, h)

# set up the ROI for tracking
roi = frame[y : y + h, x : x + w]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0.0, 60.0, 32.0)), np.array((180.0, 255.0, 255.0)))
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)

# Setup the termination criteria, either 10 iteration or move by at least 1 pt
term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)

frame_count: int = 0
while 1:
    ret, frame = cap.read()

    frame_count += 1
    if args.frame_count != -1 and frame_count > args.frame_count:
        logger.info(f"frame_count={args.frame_count} reached.")
        break

    if ret == True:  # pylint: disable=C0121
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

        # apply meanshift to get the new location
        ret, track_window = cv.meanShift(dst, track_window, term_crit)

        if args.log == 1:
            logger.info(f"frame #{frame_count}: ret={ret}, track_window={track_window}")

        # Draw it on image
        x, y, w, h = track_window
        img2 = cv.rectangle(frame, (x, y), (x + w, y + h), 255, 2)

        if args.show_gui == 1:
            cv.imshow("img2", img2)

            k = cv.waitKey(30) & 0xFF
            if k == 27:
                break
    else:
        break
