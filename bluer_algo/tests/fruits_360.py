import git
import pytest

from bluer_objects import path

from bluer_algo.env import BLUER_ALGO_FRUITS_360_REPO_ADDRESS
from bluer_journal.classes.journal import journal


@pytest.fixture
def fruits_360_checkout():
    if not path.exists(journal.path):
        git.Repo.clone_from(
            BLUER_ALGO_FRUITS_360_REPO_ADDRESS,
            journal.path,
        )
