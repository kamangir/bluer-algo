import numpy as np
import cv2 as cv
import argparse
import sys

from bluer_algo.tracker.classes.target import Target
from bluer_algo.tracker.classes.camshift import CamShiftTracker
from bluer_algo.logger import logger

parser = argparse.ArgumentParser(
    description="This sample demonstrates the camshift algorithm. \
                                              The example file can be downloaded from: \
                                              https://www.bogotobogo.com/python/OpenCV_Python/images/mean_shift_tracking/slow_traffic_small.mp4"
)
parser.add_argument(
    "--source",
    type=str,
    help="path to video file | camera.",
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
parser.add_argument(
    "--title",
    type=str,
    default="tracker",
)
args = parser.parse_args()

cap = cv.VideoCapture(0 if args.source == "camera" else args.source)

# take first frame of the video
ret, frame = cap.read()
if args.source == "camera" and not ret:
    logger.error("failed to grab initial frame from camera.")
    cap.release()
    sys.exit(1)

# setup initial location of window
if args.source == "camera":
    ret, frame = cap.read()
    success, roi = Target.select(frame)
    if not success:
        cap.release()
        cv.destroyAllWindows()
        sys.exit(1)

    x, y, w, h = roi
else:
    x, y, w, h = 300, 200, 100, 50  # simply hardcoded the values
track_window = (x, y, w, h)

tracker = CamShiftTracker(with_gui=args.show_gui == 1)
tracker.start(
    frame=frame,
    track_window=track_window,
)

# Setup the termination criteria, either 10 iteration or move by at least 1 pt
term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)

frame_count: int = 0
while 1:
    success, frame = cap.read()
    if not success:
        break

    frame_count += 1
    if args.frame_count != -1 and frame_count > args.frame_count:
        logger.info(f"frame_count={args.frame_count} reached.")
        break

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    dst = cv.calcBackProject([hsv], [0], tracker.roi_hist, [0, 180], 1)

    # apply camshift to get the new location
    ret, track_window = cv.CamShift(dst, track_window, term_crit)

    # Draw it on image
    pts = cv.boxPoints(ret)
    pts = np.intp(pts)
    output_image = cv.polylines(frame, [pts], True, 255, 2)

    if args.log == 1:
        logger.info(f"frame #{frame_count}: ret={ret}, track_window={track_window}")

    if args.show_gui == 1:
        cv.imshow(args.title, output_image)

        k = cv.waitKey(30) & 0xFF
        if k == 27:
            break

if args.source == "camera":
    cap.release()

if args.show_gui == 1:
    cv.destroyAllWindows()
