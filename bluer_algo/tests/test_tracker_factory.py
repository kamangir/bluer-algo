import pytest

from bluer_algo.tracker.classes.generic import GenericTracker
from bluer_algo.tracker.factory import LIST_OF_TRACKER_ALGO, get_tracker_class


def test_tracker_factory_LIST_OF_TRACKER_ALGO():
    for algo in LIST_OF_TRACKER_ALGO:
        assert isinstance(algo, str)


@pytest.mark.parametrize(
    [
        "algo",
        "expected_success",
    ],
    [
        [
            algo,
            True,
        ]
        for algo in LIST_OF_TRACKER_ALGO
    ]
    + [
        [
            "void",
            False,
        ]
    ],
)
def test_tracker_factory(
    algo: str,
    expected_success: bool,
):
    success, tracker_class = get_tracker_class(algo)
    assert success == expected_success

    if expected_success:
        assert tracker_class is not None
        assert issubclass(tracker_class, GenericTracker)
    else:
        assert tracker_class is None
