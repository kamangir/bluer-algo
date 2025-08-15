import pytest

from bluer_objects import storage

from bluer_algo.yolo.dataset.classes import YoloDataset
from bluer_algo import env


@pytest.mark.parametrize(
    ["object_name", "expected_valid"],
    [
        [env.BLUER_ALGO_COCO128_TEST_DATASET, True],
        ["void", False],
    ],
)
def test_yolo_dataset(
    object_name: str,
    expected_valid: bool,
):
    assert storage.download(object_name)

    dataset = YoloDataset(object_name)
    dataset.valid == expected_valid
