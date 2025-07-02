from typing import Tuple
import torch

from bluer_objects import objects

from bluer_objects.metadata import get_from_object
from bluer_algo.image_classifier.model.model import TinyCNN
from bluer_algo.logger import logger


class ImageClassifierPredictor:
    @staticmethod
    def load(object_name: str) -> Tuple[bool, "ImageClassifierPredictor"]:
        predictor = ImageClassifierPredictor()

        logger.info(
            "loading {} from {} ...".format(
                predictor.__class__.__name__,
                object_name,
            )
        )
        predictor.object_name = object_name

        predictor.metadata = get_from_object(
            object_name=predictor.object_name,
            key="model",
        )

        if "dataset" not in predictor.metadata:
            logger.error("dataset not found.")
            return False, predictor
        if "class_count" not in predictor.metadata["dataset"]:
            logger.error("dataset.class_count not found.")
            return False, predictor

        predictor.class_count = predictor.metadata["dataset"]["class_count"]
        logger.info(f"class_count: {predictor.class_count}")

        predictor.filename = objects.path_of(
            object_name=predictor.object_name,
            filename="model.pth",
        )

        try:
            predictor.model = TinyCNN(predictor.class_count)
            predictor.model.load_state_dict(
                torch.load(
                    predictor.filename,
                    map_location="cpu",
                )
            )
            predictor.model.eval()
        except Exception as e:
            logger.error(e)
            return False, predictor

        return True, predictor
