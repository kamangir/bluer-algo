import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_algo import NAME
from bluer_algo.bps.stream import Stream
from bluer_algo.logger import logger

NAME = module.name(__file__, NAME)


parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "--object_name",
    type=str,
)
parser.add_argument(
    "--sigma",
    type=float,
    default=4.0,
)
parser.add_argument(
    "--simulate",
    type=int,
    default=0,
    help="0 | 1",
)
parser.add_argument(
    "--x",
    type=float,
    default=1.0,
)
parser.add_argument(
    "--y",
    type=float,
    default=2.0,
)
parser.add_argument(
    "--z",
    type=float,
    default=3.0,
)
args = parser.parse_args()

stream = Stream.load(args.object_name)

stream.generate(
    simulate=args.simulate,
    as_dict={
        "x": args.x,
        "y": args.y,
        "z": args.z,
        "sigma": args.sigma,
    },
)

success = stream.save(args.object_name)

sys_exit(logger, NAME, "generate", success)
