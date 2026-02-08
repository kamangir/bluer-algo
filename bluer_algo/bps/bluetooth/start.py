from blueness import module

from bluer_plugin import NAME
from bluer_plugin.logger import logger


NAME = module.name(__file__, NAME)


def start(verbose: bool) -> bool:
    logger.info(
        "{}.start{}".format(
            NAME,
            " (verbose)" if verbose else "",
        )
    )

    logger.info("🪄")

    return True
