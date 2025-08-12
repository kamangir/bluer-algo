from ultralytics import YOLO

from blueness import module
from bluer_objects import objects

from bluer_algo import NAME
from bluer_algo.logger import logger


NAME = module.name(__file__, NAME)


def review(object_name: str) -> bool:
    logger.info(f"{NAME}.review({object_name})")

    model = YOLO("yolov8n.pt")

    # epochs=0 skips training, just previews
    model.train(
        data=objects.path_of(
            object_name=object_name,
            filename="data.yaml",
        ),
        epochs=0,
    )

    return True
