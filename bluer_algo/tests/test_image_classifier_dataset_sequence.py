import pytest

from bluer_objects import storage, objects

from bluer_algo.image_classifier.dataset.sequence import sequence
from bluer_algo import env


@pytest.mark.parametrize(
    ["source_object_name"],
    [
        [env.BLUER_ALGO_SWALLOW_TEST_DATASET],
    ],
)
@pytest.mark.parametrize(
    ["length"],
    [
        [2],
    ],
)
def test_image_classifier_dataset_sequence(
    source_object_name: str,
    length: int,
):
    assert storage.download(object_name=source_object_name)

    destination_object_name = objects.unique_object(
        "test_image_classifier_dataset_sequence"
    )

    success = sequence(
        source_object_name=source_object_name,
        destination_object_name=destination_object_name,
        length=length,
    )
    assert success
