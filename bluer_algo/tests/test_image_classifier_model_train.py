import pytest

from bluer_objects import storage
from bluer_objects.objects import unique_object

from bluer_algo.image_classifier.model.train import train
from bluer_algo.env import BLUER_ALGO_FRUITS_360_TEST_DATASET


@pytest.mark.parametrize(
    ["dataset_object_name"],
    [
        [BLUER_ALGO_FRUITS_360_TEST_DATASET],
    ],
)
def test_image_classifier_model_train(dataset_object_name: str):
    model_object_name = unique_object("test_image_classifier_model_train")

    assert storage.download(object_name=dataset_object_name)

    success = train(
        dataset_object_name=dataset_object_name,
        model_object_name=model_object_name,
    )

    assert success
