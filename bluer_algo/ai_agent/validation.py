from blueness import module
from bluer_objects import file, objects

from bluer_algo import NAME
from bluer_algo.logger import logger


NAME = module.name(__file__, NAME)


def complete_transcription(object_name: str) -> bool:
    logger.info(f"{NAME}.complete_transcription({object_name})")

    success, content = file.load_json(
        objects.path_of(
            object_name=object_name,
            filename="transcript.json",
        )
    )
    if not success:
        return success

    logger.info(content.get("text", "")[::-1])
    return True
