from blueness import module

from bluer_algo import NAME
from bluer_algo.image_classifier.ingest.fruits_360.types import get_types
from bluer_algo.logger import logger


NAME = module.name(__file__, NAME)


def ingest(
    object_name: str,
    type_count: int = -1,
) -> bool:
    logger.info(
        "{}.ingest -{}> {}".format(
            NAME,
            "" if type_count == -1 else f"{type_count}-type(s)-",
            object_name,
        )
    )

    fruit_types = get_types(type_count=type_count)
    if not fruit_types:
        return False

    return True
