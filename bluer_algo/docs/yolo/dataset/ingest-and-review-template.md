title:::

## full

```bash
@select coco128-$(@@timestamp)

@yolo dataset ingest \
    upload . \
    --verbose 1

@yolo dataset review \
	~download .

@upload public,zip .
@assets publish \
    extensions=png,push .
```

set:::object_name env:::BLUER_ALGO_COCO128_TEST_DATASET

assets:::get:::object_name/review.png

object:::get:::object_name

metadata:::get:::object_name

## select classes

```bash
@select coco128-$(@@timestamp)

@yolo dataset ingest \
    upload . \
    --verbose 1 \
    --classes person

@yolo dataset review \
	~download .

@upload public,zip .
@assets publish \
    extensions=png,push .
```

set:::object_name env:::BLUER_ALGO_COCO128_TEST_DATASET_PERSON

assets:::get:::object_name/review.png

object:::get:::object_name

metadata:::get:::object_name