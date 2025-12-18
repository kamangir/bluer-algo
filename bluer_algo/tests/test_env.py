from bluer_ai.tests.test_env import test_bluer_ai_env
from bluer_objects.tests.test_env import test_bluer_objects_env

from bluer_algo.tracker.factory import LIST_OF_TRACKER_ALGO
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

    assert isinstance(env.BLUER_ALGO_TRACKER_LOG_FRAME, int)
    assert env.BLUER_ALGO_TRACKER_LOG_FRAME > 0

    assert env.BLUER_ALGO_COCO128_TEST_DATASET
    assert env.BLUER_ALGO_COCO128_TEST_MODEL

    assert isinstance(env.BLUER_AI_BPS_LOOP_BEACON_LENGTH_MIN, int)
    assert isinstance(env.BLUER_AI_BPS_LOOP_BEACON_LENGTH_MAX, int)
    assert isinstance(env.BLUER_AI_BPS_LOOP_RECEIVER_LENGTH_MIN, int)
    assert isinstance(env.BLUER_AI_BPS_LOOP_RECEIVER_LENGTH_MAX, int)

    assert isinstance(env.BLUER_AI_BPS_LOOP_GREP, str)

    assert isinstance(env.BLUER_ALGO_BPS_REVIEW_TEST_OBJECT, str)

    assert env.BLUER_ALGO_TRACKER_DEFAULT_ALGO in LIST_OF_TRACKER_ALGO

    assert env.BLUER_ALGO_AI_AGENT_MACHINE_USER_NAME
    assert env.BLUER_ALGO_AI_AGENT_API_KEY
