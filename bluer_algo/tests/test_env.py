from bluer_ai.tests.test_env import test_bluer_ai_env
from bluer_objects.tests.test_env import test_bluer_objects_env

from bluer_algo import env


def test_required_env():
    test_bluer_ai_env()
    test_bluer_objects_env()


def test_bluer_algo_env():
    assert env.BLUER_ALGO_FRUITS_360_REPO_ADDRESS

    assert env.BLUER_ALGO_FRUITS_360_TEST_DATASET
    assert env.BLUER_ALGO_SWALLOW_TEST_DATASET

    assert env.BLUER_ALGO_FRUITS_360_TEST_MODEL
    assert env.BLUER_ALGO_FRUITS_360_TEST_MODEL_2000

    assert isinstance(env.BLUER_ALGO_TRACKER_LOG_PERIOD, int)
    assert env.BLUER_ALGO_TRACKER_LOG_PERIOD > 0

    assert isinstance(env.BLUER_ALGO_TRACKER_LOG_FRAME)
    assert env.BLUER_ALGO_TRACKER_LOG_FRAME > 0
