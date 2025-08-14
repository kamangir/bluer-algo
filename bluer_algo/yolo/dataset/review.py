import cv2
import os
import random
from tqdm import tqdm
import numpy as np
from typing import Dict, Any, List

from blueness import module
from bluer_options.logger import log_list_as_str
from bluer_objects import objects, file, path
from bluer_objects.logger.image import log_image_grid

from bluer_algo import NAME
from bluer_algo.yolo.dataset.classes import YoloDataset
from bluer_algo.host import signature
from bluer_algo.logger import logger


NAME = module.name(__file__, NAME)


def review(
    object_name: str,
    verbose: bool = False,
) -> bool:
    logger.info(f"{NAME}.review({object_name})")

    dataset = YoloDataset(
        object_name=object_name,
    )

    object_path = objects.object_path(object_name)

    output_dir = os.path.join(object_path, "review")
    if not path.create(output_dir):
        return False

    ...

    list_of_records = random.sample(
        dataset.list_of_records,
        min(
            3 * 4,
            len(dataset.list_of_records),
        ),
    )

    items: List[Dict[str, Any]] = []
    for record_id in tqdm(list_of_records):
        success, image = file.load_image(
            os.path.join(
                dataset.train_images_path,
                f"{record_id}.jpg",
            ),
            log=verbose,
        )
        image = np.ascontiguousarray(image)
        if not success:
            return success

        success, label_info = file.load_text(
            os.path.join(
                dataset.train_labels_path,
                f"{record_id}.txt",
            )
        )
        if not success:
            return success

        h, w = image.shape[:2]
        for line in label_info:
            cls, x, y, bw, bh = map(float, line.strip().split())
            x1, y1 = int((x - bw / 2) * w), int((y - bh / 2) * h)
            x2, y2 = int((x + bw / 2) * w), int((y + bh / 2) * h)
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(
                image,
                dataset.metadata["names"][int(cls)],
                (x1, y1 - 5),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                1,
            )

        output_filename = os.path.join(
            output_dir,
            f"{record_id}.jpg",
        )
        if not file.save_image(
            output_filename,
            image,
            log=verbose,
        ):
            return False

        items.append({"filename": output_filename})

    return log_image_grid(
        items,
        cols=4,
        rows=3,
        verbose=verbose,
        filename=objects.path_of(
            object_name=object_name,
            filename="review.png",
        ),
        header=[
            f"count: {len(dataset.list_of_records)}",
            log_list_as_str(
                title="",
                list_of_items=list(dataset.metadata["names"].values()),
                item_name_plural="class(es)",
            ),
        ],
        footer=signature(),
    )
