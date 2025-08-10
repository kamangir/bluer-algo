from typing import List

from bluer_options.terminal import show_usage, xtra

from bluer_algo.yolo.dataset.ingest import sources as ingest_sources


def help_ingest(
    tokens: List[str],
    mono: bool,
) -> str:
    options = "".join(
        [
            xtra("dryrun,", mono=mono),
            "source={},upload".format("|".join(ingest_sources)),
        ]
    )

    return show_usage(
        [
            "@yolo",
            "dataset",
            "ingest",
            f"[{options}]",
            "[-|<object-name>]",
        ],
        "ingest -> <object-name>.",
        mono=mono,
    )


help_functions = {
    "ingest": help_ingest,
}
