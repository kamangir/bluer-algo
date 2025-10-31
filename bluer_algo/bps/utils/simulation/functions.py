from blueness import module

from bluer_options import string

from bluer_algo import NAME
from bluer_algo.logger import logger


NAME = module.name(__file__, NAME)


def pretty_duration(duration: float) -> str:
    return string.pretty_duration(
        duration,
        short=True,
        largest=True,
    )


def simulate(
    object_name: str,
    length: int = 120,
    nodes: int = 3,
    ta1: float = 30,
    ta2: float = 30,
    tr1: float = 24,
    tr2: float = 36,
) -> bool:
    logger.info(
        "{}.simulating for {} on {} node(s): "
        "ta: {} - {}, "
        "tr: {} - {} "
        "-> {}".format(
            NAME,
            pretty_duration(length),
            nodes,
            pretty_duration(ta1),
            pretty_duration(ta2),
            pretty_duration(tr1),
            pretty_duration(tr2),
            object_name,
        )
    )

    logger.info("🪄")

    return True
