# Image Classifier: Dataset: Ingest

- continues https://github.com/kamangir/image-classifier-2.
- uses https://github.com/fruits-360/fruits-360-100x100

```bash
@select fruits-365-dataset-$(@@timestamp)

@algo image_classifier dataset ingest \
    clone,count=100,source=fruits_360,upload . \
    --class_count 3

@upload public,zip .
@assets publish \
    extensions=png,push .
```

set:::object_name env:::BLUER_ALGO_FRUITS_360_TEST_DATASET

assets:::get:::object_name/grid.png

object:::get:::object_name

metadata:::get:::object_name