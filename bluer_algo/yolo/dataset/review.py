from blueness import module

from bluer_algo import NAME
from bluer_algo.logger import logger


NAME = module.name(__file__, NAME)


def review(object_name: str) -> bool:
    logger.info(f"{NAME}.review({object_name})")

    logger.info("🪄")

    return True
