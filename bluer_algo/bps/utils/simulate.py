import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_algo import NAME
from bluer_algo.bps.utils.simulation.functions import simulate
from bluer_algo.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "--object_name",
    type=str,
)
parser.add_argument(
    "--length",
    type=int,
    default=120,
    help="in seconds",
)
parser.add_argument(
    "--nodes",
    type=int,
    default=3,
)
parser.add_argument(
    "--ta1",
    type=float,
    default=30,
    help="in seconds",
)
parser.add_argument(
    "--ta2",
    type=float,
    default=30,
    help="in seconds",
)
parser.add_argument(
    "--tr1",
    type=float,
    default=24,
    help="in seconds",
)
parser.add_argument(
    "--tr2",
    type=float,
    default=36,
    help="in seconds",
)
args = parser.parse_args()


success = simulate(
    object_name=args.object_name,
    length=args.length,
    nodes=args.nodes,
    ta1=args.ta1,
    ta2=args.ta2,
    tr1=args.tr1,
    tr2=args.tr2,
)

sys_exit(logger, NAME, "simulate", success)
