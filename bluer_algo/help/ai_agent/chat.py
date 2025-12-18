from typing import List

from bluer_options.terminal import show_usage


def help_validate(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@agent",
            "chat",
            "validate",
        ],
        "validate agent.",
        mono=mono,
    )


help_functions = {
    "validate": help_validate,
}
