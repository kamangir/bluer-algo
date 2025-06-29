# [image classifier](./image-classifier.md): train

uses [ingest](./image-classifier-ingest.md).

```bash
@select $BLUER_ALGO_FRUITS_360_TEST_DATASET
@select fruits-365-model-$(@@timestamp)

@algo image_classifier train \
    - .. .

🔥

@upload filename=metadata.yaml .
@upload public,zip .
@assets publish \
    extensions=png,push .
```

set:::object_name env:::BLUER_ALGO_FRUITS_360_TEST_MODEL

assets:::get:::object_name/grid.png

object:::get:::object_name

metadata:::get:::object_name