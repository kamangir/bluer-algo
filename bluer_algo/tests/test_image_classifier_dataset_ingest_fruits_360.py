from bluer_objects.objects import unique_object

from bluer_algo.image_classifier.dataset.ingest.fruits_360.ingest import ingest
from bluer_algo.tests.fruits_360 import fruits_360_checkout


def test_image_classifier_dataset_ingest_fruits_360(fruits_360_checkout):
    object_name = unique_object("test_image_classifier_dataset_ingest_fruits_360")

    success = ingest(
        object_name=object_name,
        class_count=5,
    )

    assert success
