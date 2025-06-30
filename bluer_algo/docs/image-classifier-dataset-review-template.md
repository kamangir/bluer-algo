# [image classifier](./image-classifier.md): dataset: review

🔥

uses [ingest](./image-classifier-dataset-ingest.md).

```bash
@select $BLUER_ALGO_FRUITS_360_TEST_DATASET

@algo image_classifier dataset review \
    ~download .

@assets publish \
    extensions=png,push .
```

set:::object_name env:::BLUER_ALGO_FRUITS_360_TEST_DATASET

assets:::get:::object_name/grid.png

object:::get:::object_name

metadata:::get:::object_name