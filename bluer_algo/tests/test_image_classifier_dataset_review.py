import pytest

from bluer_objects import storage

from bluer_algo.image_classifier.dataset.review import review
from bluer_algo import env


@pytest.mark.parametrize(
    ["object_name"],
    [
        [env.BLUER_ALGO_SWALLOW_TEST_DATASET],
    ],
)
def test_image_classifier_dataset_review(object_name: str):
    assert storage.download(object_name=object_name)

    success = review(
        object_name=object_name,
    )
    assert success
