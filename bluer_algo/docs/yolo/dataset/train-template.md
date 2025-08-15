title:::

```bash
@select coco128-$(@@timestamp)

@yolo dataset ingest - . \
    --classes person

@yolo dataset review \
	~download .

@upload public,zip .
@assets publish \
    extensions=png,push .

🔥

# train
```

set:::dataset_object_name coco128-2025-08-15-vd3ev4

assets:::get:::dataset_object_name/review.png

object:::get:::dataset_object_name

metadata:::get:::dataset_object_name

---

set:::model_object_name TBA

🔥