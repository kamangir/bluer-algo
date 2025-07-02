import pytest

from bluer_objects import storage

from bluer_algo.image_classifier.model.predictor import ImageClassifierPredictor
from bluer_algo import env


@pytest.mark.parametrize(
    ["dataset_object_name"],
    [
        [env.BLUER_ALGO_FRUITS_360_TEST_DATASET],
    ],
)
def test_image_classifier_model_predictor(
    model_object_name: str,
):
    assert storage.download(
        object_name=model_object_name,
    )

    success, predictor = ImageClassifierPredictor.load(
        object_name=model_object_name,
    )

    assert success

    assert isinstance(predictor.as_str(what="classes"), str)
    assert isinstance(predictor.as_str(what="void"), str)
    assert predictor.as_str(what="void") == "void not found."
    assert isinstance(predictor.signature(), list)
