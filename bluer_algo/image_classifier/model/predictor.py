from typing import Tuple, Dict
import torch
import numpy as np
import time
from PIL import Image
from torchvision import transforms

from bluer_options import string
from bluer_objects import objects
from bluer_objects.metadata import get_from_object

from bluer_algo.image_classifier.model.model import TinyCNN
from bluer_algo.logger import logger


class ImageClassifierPredictor:
    def __init__(self):
        self.class_count = 0
        self.dict_of_classes = {}
        self.model = None

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
        for thing in ["class_count", "classes"]:
            if thing not in predictor.metadata["dataset"]:
                logger.error(f"dataset.{thing} not found.")
                return False, predictor

        predictor.class_count = predictor.metadata["dataset"]["class_count"]
        predictor.dict_of_classes = predictor.metadata["dataset"]["classes"]
        logger.info(
            "{} class(es): {}".format(
                predictor.class_count,
                ", ".join(
                    "#{}: {}".format(
                        class_index,
                        predictor.dict_of_classes[class_index],
                    )
                    for class_index in range(predictor.class_count)
                ),
            )
        )

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

    def predict(
        self,
        image: np.ndarray,
        class_index: int = -1,
        object_name: str = "",
        log: bool = True,
    ) -> Tuple[bool, int, Dict]:
        # np_img is shape (H, W, 3) in RGB
        if not isinstance(image, np.ndarray):
            logger.error(f"{image.__class__.__name__} not supported.")
            return False, 0, {}

        if not (image.ndim == 3 and image.shape[2] == 3):
            logger.error("color image expected.")
            return False, 0, {}

        elapsed_time = time.time()

        try:
            # Convert to PIL for transforms
            image_ = Image.fromarray(image.astype("uint8"))

            # Apply same transform as training
            transform = transforms.Compose(
                [
                    transforms.Resize((100, 100)),
                    transforms.ToTensor(),
                ]
            )
            input_tensor = transform(image_).unsqueeze(0)  # Shape: [1, 3, 100, 100]

            with torch.no_grad():
                output = self.model(input_tensor)
                predicted_class = torch.argmax(output, dim=1).item()

            elapsed_time = time.time() - elapsed_time
        except Exception as e:
            logger.error(e)
            return False, 0, {}

        if log:
            logger.info(
                "prediction: {} [#{}] {}- took {}".format(
                    self.dict_of_classes[predicted_class],
                    predicted_class,
                    (
                        " (correct) "
                        if class_index == predicted_class or class_index == -1
                        else "<> {} [#{}] ".format(
                            self.dict_of_classes[class_index],
                            class_index,
                        )
                    ),
                    string.pretty_duration(
                        elapsed_time,
                        include_ms=True,
                        short=True,
                    ),
                )
            )

        return (
            True,
            predicted_class,
            {
                "elapsed_time": elapsed_time,
            },
        )
