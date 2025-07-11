from bluer_objects import storage
from bluer_objects.storage.policies import DownloadPolicy
from bluer_objects import objects

from bluer_algo.image_classifier.dataset.dataset import ImageClassifierDataset


def test_image_classifier_dataset_load_list_combine():
    list_of_dataset_object_names = [
        "2025-07-09-10-59-15-x9eemj",
        "2025-07-09-11-02-42-m4b3is",
    ]

    for object_name in list_of_dataset_object_names:
        assert storage.download(
            object_name=object_name,
            policy=DownloadPolicy.DOESNT_EXIST,
        )

    success, list_of_datasets = ImageClassifierDataset.load_list(
        list_of_dataset_object_names,
        log=True,
    )
    assert success
    assert len(list_of_datasets) == len(list_of_dataset_object_names)
    for dataset in list_of_datasets:
        assert isinstance(dataset, ImageClassifierDataset)

    object_name = objects.unique_object(
        "test_image_classifier_dataset_load_list_combine"
    )

    success, dataset = ImageClassifierDataset.combine(
        list_of_datasets,
        object_name=object_name,
    )
    assert success
    assert isinstance(dataset, ImageClassifierDataset)
