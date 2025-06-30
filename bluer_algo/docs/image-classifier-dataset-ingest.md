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


![image](https://github.com/kamangir/assets/blob/main/fruits-365-dataset-2025-06-30-vjuif8/grid.png?raw=true)

[fruits-365-dataset-2025-06-30-vjuif8](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/fruits-365-dataset-2025-06-30-vjuif8.tar.gz)

```yaml
dataset:
  class_count: 3
  classes:
    0: Cucumber 5
    1: Grape White 3
    2: Pineapple 1
  count: 99
  ratios:
    eval: 0.09999999999999998
    test: 0.1
    train: 0.8
  source: fruits_360
  subsets:
    eval: 10
    test: 10
    train: 79

```
