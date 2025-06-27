import pytest

from bluer_objects.objects import unique_object

from bluer_algo.image_classifier.ingest import ingest


def test_image_classifier_ingest():
    object_name = unique_object("test_image_classifier_ingest")

    success = ingest(
        object_name=object_name,
    )

    assert success
