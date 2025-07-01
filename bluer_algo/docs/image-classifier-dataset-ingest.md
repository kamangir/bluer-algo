# [image classifier](./image-classifier.md): dataset: ingest

- continues https://github.com/kamangir/image-classifier-2.
- uses https://github.com/fruits-360/fruits-360-100x100

```bash
@select fruits-365-dataset-$(@@timestamp)

@algo image_classifier dataset ingest \
    clone,count=100,source=fruits_360 . \
    --class_count 3

@upload - .
@upload public,zip .
@assets publish \
    extensions=png,push .
```


![image](https://github.com/kamangir/assets/blob/main/fruits-365-dataset-2025-07-01-fhexyt/grid.png?raw=true)

[fruits-365-dataset-2025-07-01-fhexyt](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/fruits-365-dataset-2025-07-01-fhexyt.tar.gz)

```yaml
{}

```
