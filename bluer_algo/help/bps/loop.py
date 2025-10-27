from typing import List

from bluer_options.terminal import show_usage, xtra


def help_start(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "upload"

    return show_usage(
        [
            "@bps",
            "loop",
            "start",
            f"[{options}]",
            "[.|<object-name>]",
        ],
        "start bps loop.",
        mono=mono,
    )


def help_stop(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@bps",
            "loop",
            "stop",
        ],
        "stop bps loop.",
        mono=mono,
    )


help_functions = {
    "start": help_start,
    "stop": help_stop,
}
