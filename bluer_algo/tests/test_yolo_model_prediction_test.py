import pytest

from bluer_objects import storage
from bluer_objects.objects import unique_object
from bluer_objects.storage.policies import DownloadPolicy

from bluer_algo.yolo.model.prediction_test import prediction_test
from bluer_algo import env


@pytest.mark.parametrize(
    ["dataset_object_name"],
    [
        [env.BLUER_ALGO_COCO128_TEST_DATASET],
    ],
)
@pytest.mark.parametrize(
    ["model_object_name"],
    [
        [env.BLUER_ALGO_COCO128_TEST_MODEL],
    ],
)
def test_yolo_model_prediction_test(
    dataset_object_name: str,
    model_object_name: str,
):
    prediction_object_name = unique_object("test_yolo_model_predict")

    assert storage.download(
        object_name=dataset_object_name,
        policy=DownloadPolicy.DOESNT_EXIST,
    )

    assert storage.download(
        object_name=model_object_name,
    )

    success, prediction = prediction_test(
        dataset_object_name=dataset_object_name,
        model_object_name=model_object_name,
        prediction_object_name=prediction_object_name,
    )

    assert success
    assert "elapsed_time" in prediction
    assert isinstance(prediction["elapsed_time"], float)
