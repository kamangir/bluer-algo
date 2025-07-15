import cv2
import argparse
import sys

from bluer_algo.tracker.classes.target import Target
from bluer_algo.tracker.classes.meanshift import MeanShiftTracker
from bluer_algo.logger import logger

parser = argparse.ArgumentParser(
    description="This sample demonstrates the meanshift algorithm. \
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
    "--verbose",
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

cap = cv2.VideoCapture(0 if args.source == "camera" else args.source)

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
        cv2.destroyAllWindows()
        sys.exit(1)

    x, y, w, h = roi
else:
    x, y, w, h = 300, 200, 100, 50  # simply hardcoded the values
track_window = (x, y, w, h)

tracker = MeanShiftTracker(with_gui=args.show_gui == 1)
tracker.start(
    frame=frame,
    track_window=track_window,
)

frame_count: int = 0
while 1:
    success, frame = cap.read()
    if not success:
        break

    frame_count += 1
    if args.frame_count != -1 and frame_count > args.frame_count:
        logger.info(f"frame_count={args.frame_count} reached.")
        break

    ret, track_window, output_image = tracker.track(
        frame=frame,
        track_window=track_window,
    )

    if args.verbose == 1:
        logger.info(f"frame #{frame_count}: ret={ret}, track_window={track_window}")

    if args.show_gui == 1:
        cv2.imshow(args.title, output_image)

        k = cv2.waitKey(30) & 0xFF
        if k == 27:
            break

if args.source == "camera":
    cap.release()

if args.show_gui == 1:
    cv2.destroyAllWindows()
