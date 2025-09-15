import pytest
import pandas as pd
import numpy as np

from bluer_objects import storage, file, objects
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
    assert dataset.valid == expected_valid

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
        thing = dataset.path_of(suffix=suffix, what=what)
        assert thing.startswith(startswith)
        assert thing.endswith(suffix)

    assert dataset.list_of_records
    record_id = dataset.list_of_records[0]

    assert dataset.review()

    assert isinstance(dataset.signature(), list)

    for suffix, what, startswith in zip(
        [
            f"{record_id}.jpg",
            f"{record_id}.txt",
        ],  # suffix
        [
            "image",
            "label",
        ],  # what
        [
            dataset.train_images_path,
            dataset.train_labels_path,
        ],  # startswith
    ):
        thing = dataset.path_of_record(
            what=what,
            record_id=record_id,
        )

        assert thing.startswith(startswith)
        assert thing.endswith(suffix)

    for record_id_, expected_success in zip(
        [record_id, "void"],
        [True, False],
    ):
        success, df = dataset.load_label(record_id=record_id_)
        assert success == expected_success

        if not expected_success:
            continue

        assert isinstance(df, pd.DataFrame)

        assert dataset.save_label(
            record_id=record_id,
            df=df,
        )

        assert file.delete(
            dataset.path_of_record(
                what="label",
                record_id=record_id,
            )
        )

    for record_id_, expected_success in zip(
        [record_id, "void"],
        [True, False],
    ):
        success, image = dataset.load_image(record_id=record_id_)
        assert success == expected_success

        if not expected_success:
            continue

        assert isinstance(image, np.ndarray)
