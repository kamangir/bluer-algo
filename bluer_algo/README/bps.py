from bluer_objects.README.items import ImageItems
from bluer_objects.README.consts import assets_url


assets2 = assets_url(
    suffix="bps",
    volume=2,
)


docs = [
    {
        "path": "../docs/bps",
        "items": ImageItems({f"{assets2}/{index+1:02}.png": "" for index in range(4)}),
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
