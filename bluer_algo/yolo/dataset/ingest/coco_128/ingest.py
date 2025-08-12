from blueness import module
from bluer_objects import file, objects

from bluer_algo import NAME
from bluer_algo.logger import logger


NAME = module.name(__file__, NAME)


def ingest(
    object_name: str,
    log: bool = True,
    verbose: bool = False,
) -> bool:
    logger.info(
        "{}.ingest -> {}".format(
            NAME,
            object_name,
        )
    )

    return file.copy(
        file.absolute(
            "../../../../assets/coco_128.yaml",
            file.path(__file__),
        ),
        objects.path_of(
            object_name=object_name,
            filename="data.yaml",
        ),
        log=log,
    )
