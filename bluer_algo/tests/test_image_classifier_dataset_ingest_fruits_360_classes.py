from bluer_algo.image_classifier.dataset.ingest.fruits_360.classes import get_classes
from bluer_algo.tests.fruits_360 import fruits_360_checkout


def test_image_classifier_dataset_ingest_fruits_360_classes(fruits_360_checkout):
    dict_of_classes = get_classes(class_count=10)

    assert isinstance(dict_of_classes, dict)
    assert dict_of_classes
    assert 0 in dict_of_classes
    assert isinstance(dict_of_classes[0], str)
