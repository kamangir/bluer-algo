from bluer_algo.image_classifier.ingest.fruits_360.types import get_types
from bluer_algo.tests.fruits_360 import fruits_360_checkout


def test_image_classifier_ingest_fruits_360_types(fruits_360_checkout):
    fruit_types = get_types(type_count=10)

    assert isinstance(fruit_types, dict)
    assert fruit_types
    assert 0 in fruit_types
    assert isinstance(fruit_types[0], str)
