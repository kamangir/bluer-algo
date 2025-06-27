# [image classifier](./image-classifier.md): ingest

- continues https://github.com/kamangir/image-classifier-2.
- uses https://github.com/fruits-360/fruits-360-100x100

```bash
@select fruits-365-$(@@timestamp)

@algo image_classifier ingest \
    clone,count=100,source=fruits_360 . \
    --class_count 10

@upload filename=metadata.yaml .
@upload public,zip .
```

set:::object_name fruits-365-2025-06-27-ualwd6

object:::get:::object_name

metadata:::get:::object_name

- 🔥