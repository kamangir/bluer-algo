# yolo: dataset: train

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


![image](https://github.com/kamangir/assets/blob/main/TBA/review.png?raw=true)

[TBA](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/TBA.tar.gz)

```yaml
{}

```
