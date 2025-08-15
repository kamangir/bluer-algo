import pytest
from typing import List

from bluer_objects import storage
from bluer_objects.storage.policies import DownloadPolicy

from bluer_algo.yolo.dataset.classes import YoloDataset
from bluer_algo import env


@pytest.mark.parametrize(
    ["object_name", "classes", "expected_success"],
    [
        [env.BLUER_ALGO_COCO128_TEST_DATASET, ["person", "void"], True],
        [env.BLUER_ALGO_COCO128_TEST_DATASET, ["person", "void"], False],
        [env.BLUER_ALGO_COCO128_TEST_DATASET, ["person", "boat"], True],
        [env.BLUER_ALGO_COCO128_TEST_DATASET, ["person"], True],
    ],
)
def test_yolo_dataset_filter(
    object_name: str,
    classes: List[str],
    expected_success: bool,
):
    assert storage.download(
        object_name,
        policy=DownloadPolicy.DOESNT_EXIST,
    )

    dataset = YoloDataset(object_name)
    assert dataset.valid

    success = dataset.filter(classes=classes)
    success == expected_success

    if expected_success:
        dataset = YoloDataset(object_name)
        assert dataset.valid
