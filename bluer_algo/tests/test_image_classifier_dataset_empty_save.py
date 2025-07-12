from bluer_objects import objects

from bluer_algo.image_classifier.dataset.dataset import ImageClassifierDataset


def test_image_classifier_dataset_empty_save():
    object_name = objects.unique_object("test_image_classifier_dataset_empty_save")

    dataset = ImageClassifierDataset(
        dict_of_classes={0: "this", 1: "that"},
        object_name=object_name,
    )

    assert dataset.save()
