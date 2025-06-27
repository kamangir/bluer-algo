import os
from typing import Dict

from blueness import module
from bluer_options.logger import log_list
from bluer_objects import path
from bluer_objects.env import abcli_path_git

from bluer_algo import NAME
from bluer_algo.logger import logger


NAME = module.name(__file__, NAME)


def get_types(
    type_count: int = -1,
) -> Dict[str, int]:
    logger.info(
        "{}.get_types{}".format(
            NAME,
            "" if type_count == -1 else f": {type_count} type(s)",
        )
    )

    repo_path = os.path.join(abcli_path_git, "fruits-360-100x100/Training")
    logger.info(f"reading {repo_path} ...")

    list_of_types = sorted([path.name(path_) for path_ in path.list_of(repo_path)])
    if type_count != -1:
        list_of_types = list_of_types[:type_count]
    log_list(
        logger,
        "found",
        list_of_types,
        "type(s)",
        itemize=False,
    )

    return {
        fruit_type: fruit_index
        for fruit_type, fruit_index in zip(
            list_of_types,
            range(len(list_of_types)),
        )
    }
