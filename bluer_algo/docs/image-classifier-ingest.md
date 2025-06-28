# [image classifier](./image-classifier.md): ingest

- continues https://github.com/kamangir/image-classifier-2.
- uses https://github.com/fruits-360/fruits-360-100x100

```bash
@select fruits-365-dataset-$(@@timestamp)

@algo image_classifier ingest \
    clone,count=100,source=fruits_360 . \
    --class_count 3

@upload filename=metadata.yaml .
@upload public,zip .
@assets publish \
    extensions=png,push .
```


![image](https://github.com/kamangir/assets/blob/main/fruits-365-dataset-2025-06-28-rtpost/grid.png?raw=true)

[fruits-365-dataset-2025-06-28-rtpost](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/fruits-365-dataset-2025-06-28-rtpost.tar.gz)

```yaml
dataset:
  class_count: 3
  classes:
    0: Apple Granny Smith 1
    1: Lychee 1
    2: Tomato Cherry Maroon 1
  count: 100
  ratios:
    eval: 0.09999999999999998
    test: 0.1
    train: 0.8
  source: fruits_360
  subsets:
    eval: 14
    test: 11
    train: 74

```
