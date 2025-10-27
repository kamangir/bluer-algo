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
                f"{assets2}/01.png": "",
                f"{assets2}/03.png": "",
                f"{assets2}/02.png": "",
                f"{assets2}/05.png": "",
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
        "loop",
        "mathematics",
        "mathematics-timing",
        "mathematics-localization",
    ]
]
