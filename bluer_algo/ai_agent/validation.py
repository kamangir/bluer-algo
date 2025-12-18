from blueness import module
from bluer_objects import file, objects
from bluer_objects.metadata import post_to_object

from bluer_algo import NAME
from bluer_algo.logger import logger


NAME = module.name(__file__, NAME)


def complete_transcription(
    object_name: str,
    filename: str,
    language: str = "fa",
) -> bool:
    filename = file.name_and_extension(filename)

    logger.info(
        "{}.complete_transcription({}/{}) [{}]".format(
            NAME,
            object_name,
            filename,
            language,
        )
    )

    success, content = file.load_json(
        objects.path_of(
            object_name=object_name,
            filename="transcript.json",
        ),
        default={},
    )
    if not success:
        return success

    if not isinstance(content, dict):
        logger.error("content is not a dict")
        return False

    text = content.get("text", "")
    if language == "fa":
        text = text[::-1]

    logger.info(text)

    return post_to_object(
        object_name,
        filename,
        text,
    )
