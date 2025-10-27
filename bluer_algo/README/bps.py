from bluer_objects.README.items import ImageItems
from bluer_objects.README.consts import assets_url


assets2 = assets_url(
    suffix="bps",
    volume=2,
)


docs = [
    {
        "path": "../docs/bps",
        "cols": 2,
        "items": ImageItems(
            {
                f"{assets2}/2.png": "",
                f"{assets2}/0.png": "",
                f"{assets2}/1.png": "",
                f"{assets2}/3.png": "",
            }
        ),
    }
] + [
    {
        "path": f"../docs/bps/{doc}.md",
    }
    for doc in [
        "literature",
        "test-introspect",
        "beacon-receiver",
        "mathematics",
    ]
]
