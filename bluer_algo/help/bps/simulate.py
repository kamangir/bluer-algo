from typing import List

from bluer_options.terminal import show_usage, xtra


def help_timing(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "upload"

    args = [
        "[--length <120>]",
        "[--nodes <3>]",
        "[--ta1 <30>]",
        "[--ta2 <30>]",
        "[--tr1 <24>]",
        "[--tr2 <36>]",
    ]

    return show_usage(
        [
            "@bps",
            "simulate",
            "timing",
            f"[{options}]",
            "[-|<object-name>]",
        ]
        + args,
        "simulate timing.",
        mono=mono,
    )


help_functions = {
    "timing": help_timing,
}
