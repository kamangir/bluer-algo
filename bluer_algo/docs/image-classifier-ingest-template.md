# [image classifier](./image-classifier.md): ingest

- continues https://github.com/kamangir/image-classifier-2.
- uses https://github.com/fruits-360/fruits-360-100x100

```bash
@select fruits-365-dataset-$(@@timestamp)

@algo image_classifier ingest \
    clone,count=100,source=fruits_360 . \
    --class_count 3

@upload filename=metadata.yaml .
@upload public,zip .
@assets publish \
    extensions=png,push .
```

set:::object_name fruits-365-dataset-2025-06-28-rtpost

assets:::get:::object_name/grid.png

object:::get:::object_name

metadata:::get:::object_name