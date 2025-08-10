from blueness import module

from bluer_plugin import NAME
from bluer_plugin.logger import logger


NAME = module.name(__file__, NAME)


def ingest_coco128(arg: str) -> bool:
    logger.info(f"{NAME}.ingest_coco128: arg={arg}")
    return True
