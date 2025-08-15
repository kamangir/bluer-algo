import pytest

from bluer_objects import storage
from bluer_objects import objects
from bluer_objects.storage.policies import DownloadPolicy

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
    assert storage.download(
        object_name,
        policy=DownloadPolicy.DOESNT_EXIST,
    )

    dataset = YoloDataset(object_name)
    dataset.valid == expected_valid

    if not expected_valid:
        return

    for suffix, what, startswith in zip(
        [
            "this.yaml",
            "this",
            "this.jpg",
            "this.txt",
        ],  # suffix
        [
            "filename",
            "dir",
            "image",
            "label",
        ],  # what
        [
            objects.object_path(object_name),
            objects.object_path(object_name),
            dataset.train_images_path,
            dataset.train_labels_path,
        ],  # startswith
    ):
        filename = dataset.path_of(suffix=suffix, what=what)
        assert filename.startswith(startswith)
        assert filename.endswith(suffix)
