from typing import List

from bluer_options.terminal import show_usage, xtra


def help_start(
    tokens: List[str],
    mono: bool,
) -> str:
    options = xtra("~python,verbose", mono=mono)

    return show_usage(
        [
            "@bps",
            "bluetooth",
            "start",
            f"[{options}]",
        ],
        "start bluetooth.",
        mono=mono,
    )


help_functions = {
    "start": help_start,
}
