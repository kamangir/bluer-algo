from blueness import module

from bluer_plugin import NAME
from bluer_plugin.logger import logger


NAME = module.name(__file__, NAME)


def start() -> bool:
    logger.info(f"{NAME}.start")
    return True
