import pytest

from bluer_objects import storage

from bluer_algo.image_classifier.dataset.review import review
from bluer_algo.env import BLUER_ALGO_FRUITS_360_TEST_DATASET


@pytest.mark.parametrize(
    ["object_name"],
    [
        ["2025-07-09-10-59-15-x9eemj"],
    ],
)
def test_image_classifier_dataset_review(object_name: str):
    assert storage.download(object_name=object_name)

    success = review(
        object_name=object_name,
    )
    assert success
