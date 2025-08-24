# yolo: model: validation

```bash
@select coco128-$(@@timestamp)

@yolo dataset ingest - . \
    --classes person

@yolo dataset review \
	~download .

@upload public,zip .
@assets publish \
    extensions=png,push .

@select coco128-model-$(@@timestamp)

@yolo model train \
	~download .. .

🔥

# train
```


![image](https://github.com/kamangir/assets/blob/main/coco128-2025-08-15-vd3ev4/review.png?raw=true)

[coco128-2025-08-15-vd3ev4](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/coco128-2025-08-15-vd3ev4.tar.gz)

```yaml
dataset:
  count: 61
names:
  0: person
path: ./coco128
source: coco_128
train: images/train2017
val: images/train2017

```

---


🔥
