from blueness import module

from bluer_algo import NAME
from bluer_algo.logger import logger


NAME = module.name(__file__, NAME)


def ingest(
    object_name: str,
    verbose: bool = False,
) -> bool:
    logger.info(
        "{}.ingest -> {}".format(
            NAME,
            object_name,
        )
    )

    logger.info("🪄")

    return True
