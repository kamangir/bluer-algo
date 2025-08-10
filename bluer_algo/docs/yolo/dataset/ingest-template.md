title:::

🔥

```bash
@select coco128-$(@@timestamp)

@algo yolo dataset ingest \
    ~upload . \
    --verbose 1

@upload public,zip .
@assets publish \
    extensions=png,push .
```

set:::object_name env:::BLUER_ALGO_COCO128_TEST_DATASET

assets:::get:::object_name/grid.png

object:::get:::object_name

metadata:::get:::object_name