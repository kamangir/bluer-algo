# [image classifier](./image-classifier.md): ingest

- continues https://github.com/kamangir/image-classifier-2.
- uses https://github.com/fruits-360/fruits-360-100x100

```bash
@select fruits-365-dataset-$(@@timestamp)

@algo image_classifier ingest \
    clone,count=100,source=fruits_360 . \
    --class_count 3

@upload - .
@upload public,zip .
@assets publish \
    extensions=png,push .
```


![image](https://github.com/kamangir/assets/blob/main/fruits-365-dataset-2025-06-30-g9i5jy/grid.png?raw=true)

[fruits-365-dataset-2025-06-30-g9i5jy](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/fruits-365-dataset-2025-06-30-g9i5jy.tar.gz)

```yaml
dataset:
  class_count: 3
  classes:
    0: Cactus fruit 1
    1: Pear Forelle 1
    2: Plum 2
  count: 99
  ratios:
    eval: 0.09999999999999998
    test: 0.1
    train: 0.8
  source: fruits_360
  subsets:
    eval: 13
    test: 6
    train: 80

```
