import pytest


from bluer_algo.image_classifier.dataset.review import review
from bluer_algo.env import BLUER_ALGO_FRUITS_360_TEST_DATASET


@pytest.mark.parametrize(
    ["object_name"],
    [
        [BLUER_ALGO_FRUITS_360_TEST_DATASET],
    ],
)
def test_image_classifier_dataset_review(object_name: str):
    success = review(
        object_name=object_name,
    )

    assert success
