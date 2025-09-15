from typing import Tuple, Dict

from bluer_algo.logger import logger


def prediction_test(
    dataset_object_name: str,
    model_object_name: str,
    prediction_object_name: str = "",
) -> Tuple[bool, Dict]:
    logger.info("🪄")

    return True, {
        "elapsed_time": 0.0,
    }
