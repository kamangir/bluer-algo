from bluer_objects.README.items import ImageItems
from bluer_objects.README.consts import assets_url


assets2 = assets_url(
    suffix="anchor",
    volume=2,
)


docs = [
    {
        "path": "../docs/lora-keyboard.md",
        "items": ImageItems(
            {
                f"{assets2}/03.png": "",
            }
        ),
    }
]
