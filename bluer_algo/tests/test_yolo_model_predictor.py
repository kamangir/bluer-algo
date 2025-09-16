import pytest

from bluer_objects import storage

from bluer_algo.yolo.model.predictor import YoloPredictor
from bluer_algo import env


@pytest.mark.parametrize(
    ["model_object_name"],
    [
        [env.BLUER_ALGO_COCO128_TEST_MODEL],
    ],
)
def test_yolo_model_predictor(
    model_object_name: str,
):
    assert storage.download(
        object_name=model_object_name,
    )

    success, predictor = YoloPredictor.load(
        object_name=model_object_name,
    )

    assert success

    assert isinstance(predictor, YoloPredictor)
    assert isinstance(predictor.model_size, str)
