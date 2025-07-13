# [image classifier](../): Model: Train

## small dataset

uses [ingest](../image_classifier/ingest.md).

```bash
@select $BLUER_ALGO_FRUITS_360_TEST_DATASET
@select fruits-365-model-$(@@timestamp)

@algo image_classifier model train \
    upload .. .

@upload public,zip .
@assets publish \
    extensions=png,push .
```

set:::object_name env:::BLUER_ALGO_FRUITS_360_TEST_MODEL

assets:::get:::object_name/loss.png

assets:::get:::object_name/evaluation.png

assets:::get:::object_name/confusion_matrix.png

object:::get:::object_name

metadata:::get:::object_name

## large dataset

```bash
@select fruits-365-dataset-2000-$(@@timestamp)

@algo image_classifier dataset ingest \
    clone,count=10000,source=fruits_360 . \
    --class_count 3

@select fruits-365-model-2000-$(@@timestamp)

@algo image_classifier model train \
    ~download,upload .. .

@upload public,zip .
@assets publish \
    extensions=png,push .
```

set:::object_name env:::BLUER_ALGO_FRUITS_360_TEST_MODEL_2000

assets:::get:::object_name/loss.png

assets:::get:::object_name/evaluation.png

assets:::get:::object_name/confusion_matrix.png

object:::get:::object_name

metadata:::get:::object_name