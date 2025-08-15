title:::

🔥

```bash
@select coco128-$(@@timestamp)

@yolo dataset ingest - . \
    --classes person

@yolo dataset review \
	~download .

@upload public,zip .
@assets publish \
    extensions=png,push .
```

set:::object_name TBA

assets:::get:::object_name/review.png

object:::get:::object_name

metadata:::get:::object_name