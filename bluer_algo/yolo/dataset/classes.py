import os

from blueness import module
from bluer_options.logger import log_list
from bluer_objects import objects, file, path

from bluer_algo import NAME
from bluer_algo.logger import logger

NAME = module.name(__file__, NAME)


class YoloDataset:
    def __init__(
        self,
        object_name: str,
        log: bool = True,
    ):
        self.object_name = object_name

        self.valid, self.metadata = file.load_yaml(
            objects.path_of(
                object_name=object_name,
                filename="data.yaml",
            )
        )

        object_path = objects.object_path(object_name)

        self.train_images_path = os.path.join(
            path.absolute(
                self.metadata["path"],
                object_path,
            ),
            self.metadata["train"],
        )

        self.train_labels_path = self.train_images_path.replace(
            "images",
            "labels",
        )

        list_of_images = [
            file.name(filename)
            for filename in file.list_of(
                os.path.join(self.train_images_path, "*.jpg"),
                recursive=False,
            )
        ]
        if log:
            logger.info(f"found {len(list_of_images)} image(s).")

        list_of_labels = [
            file.name(filename)
            for filename in file.list_of(
                os.path.join(self.train_labels_path, "*.txt"),
                recursive=False,
            )
        ]
        if log:
            logger.info(f"found {len(list_of_labels)} label(s).")

        self.list_of_records = [
            record_id for record_id in list_of_images if record_id in list_of_labels
        ]

        missing_images = [
            record_id
            for record_id in list_of_images
            if record_id not in self.list_of_records
        ]
        if missing_images and log:
            log_list(logger, "missing", missing_images, "image(s)", itemize=False)

        missing_labels = [
            record_id
            for record_id in list_of_labels
            if record_id not in self.list_of_records
        ]
        if missing_labels and log:
            log_list(logger, "missing", missing_labels, "label(s)", itemize=False)

        if log:
            logger.info(
                "{}: {} record(s)".format(
                    NAME,
                    len(self.list_of_records),
                )
            )
