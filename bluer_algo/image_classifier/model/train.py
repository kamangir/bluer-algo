from blueness import module

from bluer_algo import NAME
from bluer_algo.image_classifier.dataset.classes import ImageClassifierDataset
from bluer_algo.logger import logger


NAME = module.name(__file__, NAME)


def train(
    dataset_object_name: str,
    model_object_name: str,
) -> bool:
    logger.info(
        "{}.train: {} -> {}".format(
            NAME,
            dataset_object_name,
            model_object_name,
        )
    )

    success, dataset = ImageClassifierDataset.load(
        object_name=dataset_object_name,
    )
    if not success:
        return success

    return True
