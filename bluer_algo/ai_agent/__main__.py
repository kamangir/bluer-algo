import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_algo import NAME
from bluer_algo import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
args = parser.parse_args()

success = None

sys_exit(logger, NAME, args.task, success)
