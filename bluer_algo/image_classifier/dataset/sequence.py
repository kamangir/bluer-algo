from blueness import module

from bluer_algo import NAME
from bluer_algo.logger import logger

NAME = module.name(__file__, NAME)


def sequence(
    source_object_name: str,
    destination_object_name: str,
    length: str,
) -> bool:
    logger.info(
        "{}.sequence: {} -{}X-> {}".format(
            NAME,
            source_object_name,
            length,
            destination_object_name,
        )
    )

    logger.info("🪄")

    return True
