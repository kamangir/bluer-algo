import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_algo import NAME
from bluer_algo.ai_agent.validation import complete_transcription
from bluer_algo.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="complete_transcription",
)
parser.add_argument(
    "--object_name",
    type=str,
)
parser.add_argument(
    "--filename",
    type=str,
)
parser.add_argument(
    "--language",
    type=str,
    default="fa",
    help="en | fa",
)
args = parser.parse_args()

success = False
if args.task == "complete_transcription":
    success = complete_transcription(
        object_name=args.object_name,
        filename=args.filename,
        language=args.language,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
