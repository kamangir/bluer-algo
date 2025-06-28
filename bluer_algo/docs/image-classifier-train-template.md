# [image classifier](./image-classifier.md): train

uses [ingest](./image-classifier-ingest.md).

```bash
@select fruits-365-dataset-2025-06-28-rtpost
@select fruits-365-model-$(@@timestamp)

@algo image_classifier train \
    - .. .

🔥

@upload filename=metadata.yaml .
@upload public,zip .
@assets publish \
    extensions=png,push .
```

set:::object_name TBA

assets:::get:::object_name/grid.png

object:::get:::object_name

metadata:::get:::object_name