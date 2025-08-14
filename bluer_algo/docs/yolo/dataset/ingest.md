# yolo: dataset: ingest

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


![image](https://github.com/kamangir/assets/blob/main/coco128-2025-08-14-m0401y/review.png?raw=true)

[coco128-2025-08-14-m0401y](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/coco128-2025-08-14-m0401y.tar.gz)

```yaml
{}

```
