import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_algo import NAME
from bluer_algo.bps.bluetooth.start import start
from bluer_algo.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="start",
)
args = parser.parse_args()

success = False
if args.task == "start":
    success = start()
else:
    success = None

sys_exit(logger, NAME, args.task, success)
