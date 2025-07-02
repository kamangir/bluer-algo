import pytest

from bluer_objects import storage
from bluer_objects.objects import unique_object

from bluer_algo.image_classifier.model.train import train
from bluer_algo.image_classifier.dataset.dataset import ImageClassifierDataset
from bluer_algo.image_classifier.model.predictor import ImageClassifierPredictor
from bluer_algo import env


@pytest.mark.parametrize(
    ["dataset_object_name"],
    [
        [env.BLUER_ALGO_FRUITS_360_TEST_DATASET],
    ],
)
@pytest.mark.parametrize(
    ["model_object_name"],
    [
        [env.BLUER_ALGO_FRUITS_360_TEST_MODEL],
    ],
)
def test_image_classifier_model_predict(
    dataset_object_name: str,
    model_object_name: str,
):
    prediction_object_name = unique_object("test_image_classifier_model_predict")

    assert storage.download(
        object_name=dataset_object_name,
    )

    success, dataset = ImageClassifierDataset.load(
        object_name=dataset_object_name,
    )
    assert success

    success, predictor = ImageClassifierPredictor.load(
        object_name=model_object_name,
    )
    assert success

    success, class_index, image = dataset.sample(
        subset="test",
    )
    assert success

    success, predicted_class, prediction_metadata = predictor.predict(
        image=image,
        class_index=class_index,
        object_name=prediction_object_name,
        log=True,
    )
    assert success
    assert isinstance(predicted_class, int)
    assert "elapsed_time" in prediction_metadata
