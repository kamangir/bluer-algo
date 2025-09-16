from bluer_objects import objects

from bluer_algo.yolo.dataset.classes import YoloDataset


def test_yolo_dataset_create():
    object_name = objects.unique_object("test_yolo_dataset_create")

    dataset = YoloDataset(
        object_name=object_name,
        create=True,
    )

    assert dataset.valid == True
    assert dataset.empty
