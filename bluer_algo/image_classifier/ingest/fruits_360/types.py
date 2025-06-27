from typing import Dict, Tuple

from blueness import module

from bluer_algo import NAME
from bluer_algo.logger import logger


NAME = module.name(__file__, NAME)


def get_types(
    type_count: int = -1,
) -> Tuple[bool, Dict[str, int]]:
    logger.info(
        "{}.get_types{}".format(
            NAME,
            "" if type_count == -1 else f": {type_count} type(s)",
        )
    )

    return True, {}
