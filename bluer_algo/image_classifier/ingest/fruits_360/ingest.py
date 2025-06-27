import os
from tqdm import trange, tqdm

from blueness import module
from bluer_objects import path, objects, file

from bluer_algo import NAME
from bluer_algo.image_classifier.ingest.fruits_360.types import get_types
from bluer_algo.env import BLUER_ALGO_FRUITS_360_REPO_PATH
from bluer_algo.logger import logger


NAME = module.name(__file__, NAME)


def ingest(
    object_name: str,
    count: int = 100,
    type_count: int = -1,
    test_ratio: float = 0.1,
    train_ratio: float = 0.8,
    verbose: bool = True,
) -> bool:
    eval_ratio = 1 - test_ratio - train_ratio
    if eval_ratio < 0:
        logger.error(f"eval_ratio = {eval_ratio:.2f} < 0")
        return False

    logger.info(
        "{}.ingest -{}{}> {}".format(
            NAME,
            "" if type_count == -1 else f"{type_count}-type(s)-",
            f"{count}-record(s)-",
            object_name,
        )
    )
    logger.info(
        "ratios: train={:.2f}, eval={:.2f}, test={:.2f}".format(
            train_ratio,
            eval_ratio,
            test_ratio,
        )
    )

    fruit_types = get_types(
        type_count=count if type_count == -1 else type_count,
    )
    if type_count == -1:
        type_count = len(fruit_types)

    record_count_per_type = int(count / type_count)
    for type_index in trange(type_count):
        record_type = fruit_types[type_index]

        logger.info(f"ingesting {record_type}")

        list_of_filenames = file.list_of(
            os.path.join(
                BLUER_ALGO_FRUITS_360_REPO_PATH,
                "Training",
                record_type,
                "*.jpg",
            )
        )
        list_of_filenames = list_of_filenames[:record_count_per_type]

        for filename in tqdm(list_of_filenames):
            if not file.copy(
                filename,
                objects.path_of(
                    object_name=object_name,
                    filename=file.name_and_extension(filename),
                ),
                log=verbose,
            ):
                return False

    ...

    return True
