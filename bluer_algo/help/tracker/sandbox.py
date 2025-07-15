from typing import List

from bluer_options.terminal import show_usage, xtra


def help_sandbox(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            "algo=camshift|meanshift",
            xtra(",~download", mono=mono),
        ]
    )

    return show_usage(
        [
            "@algo",
            "tracker",
            "sandbox",
            f"[{options}]",
        ],
        "run sandbox/algo.",
        mono=mono,
    )
