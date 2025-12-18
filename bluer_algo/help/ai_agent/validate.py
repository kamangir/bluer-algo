from typing import List

from bluer_options.terminal import show_usage, xtra


def help_validate(
    tokens: List[str],
    mono: bool,
) -> str:

    return show_usage(
        [
            "@agent",
            "validate",
        ],
        "validate agent.",
        mono=mono,
    )
