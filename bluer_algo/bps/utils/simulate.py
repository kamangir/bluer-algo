import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_algo import NAME
from bluer_algo.bps.simulation.timing.specs import Specs as simulate_specs
from bluer_algo.bps.simulation.timing.functions import simulate as simulate_timing
from bluer_algo.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    default="timing",
    help="timing",
)
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
    "--tao",
    type=int,
    default=1,
    help="in seconds",
)
parser.add_argument(
    "--tac",
    type=int,
    default=0,
    help="in seconds",
)
parser.add_argument(
    "--tro",
    type=int,
    default=3,
    help="in seconds",
)
parser.add_argument(
    "--trc",
    type=int,
    default=1,
    help="in seconds",
)
parser.add_argument(
    "--ta1",
    type=int,
    default=30,
    help="in seconds",
)
parser.add_argument(
    "--ta2",
    type=int,
    default=30,
    help="in seconds",
)
parser.add_argument(
    "--tr1",
    type=int,
    default=24,
    help="in seconds",
)
parser.add_argument(
    "--tr2",
    type=int,
    default=36,
    help="in seconds",
)
args = parser.parse_args()

success = False
if args.task == "timing":
    success = simulate_timing(
        object_name=args.object_name,
        length=args.length,
        nodes=args.nodes,
        specs=simulate_specs(
            tao=args.tao,
            tac=args.tac,
            tro=args.tro,
            trc=args.trc,
            ta1=args.ta1,
            ta2=args.ta2,
            tr1=args.tr1,
            tr2=args.tr2,
        ),
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
