import git
import pytest

from bluer_objects import path

from bluer_algo.env import (
    BLUER_ALGO_FRUITS_360_REPO_ADDRESS,
    BLUER_ALGO_FRUITS_360_REPO_PATH,
)


@pytest.fixture
def fruits_360_checkout():
    if not path.exists(BLUER_ALGO_FRUITS_360_REPO_PATH):
        git.Repo.clone_from(
            BLUER_ALGO_FRUITS_360_REPO_ADDRESS,
            BLUER_ALGO_FRUITS_360_REPO_PATH,
        )
