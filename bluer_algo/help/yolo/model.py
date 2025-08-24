from typing import List

from bluer_options.terminal import show_usage, xtra


def help_train(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("~download,upload", mono=mono)

    args = []

    return show_usage(
        [
            "@yolo",
            "model",
            "train",
            f"[{options}]",
            "[.|<dataset-object-name>]",
            "[-|<model-object-name>]",
        ]
        + args,
        "train.",
        mono=mono,
    )


help_functions = {
    "train": help_train,
}
