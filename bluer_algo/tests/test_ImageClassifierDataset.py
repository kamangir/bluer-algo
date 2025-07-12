import pytest
import numpy as np

from bluer_algo.env import BLUER_ALGO_FRUITS_360_TEST_DATASET
from bluer_objects import storage
from bluer_algo.image_classifier.dataset.dataset import ImageClassifierDataset


@pytest.mark.parametrize(
    ["object_name"],
    [
        ["2025-07-09-10-59-15-x9eemj"],
    ],
)
def test_ImageClassifierDataset(object_name: str):
    assert storage.download(object_name=object_name)

    success, dataset = ImageClassifierDataset.load(object_name=object_name)
    assert success
    assert isinstance(dataset, ImageClassifierDataset)

    assert isinstance(dataset.as_str(what="classes"), str)
    assert isinstance(dataset.as_str(what="subsets"), str)
    assert isinstance(dataset.as_str(what="void"), str)
    assert dataset.as_str(what="void") == "void not found."

    assert isinstance(dataset.class_count, int)
    assert dataset.class_count > 0

    assert isinstance(dataset.count, int)
    assert dataset.count > 0

    assert isinstance(dataset.dict_of_classes, dict)

    assert isinstance(dataset.dict_of_class_counts, dict)

    assert isinstance(dataset.dict_of_subsets, dict)

    assert dataset.log_image_grid()

    assert dataset.generate_timeline()

    assert dataset.save()

    assert isinstance(dataset.signature(), list)

    for subset in dataset.dict_of_subsets.keys():
        success, class_index, image = dataset.sample(subset=subset)
        assert success
        assert isinstance(class_index, int)
        assert isinstance(image, np.ndarray)
