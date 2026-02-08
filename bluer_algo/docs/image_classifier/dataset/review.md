# image-classifier: dataset: review

uses [ingest](./ingest.md).

```bash
@select $BLUER_ALGO_FRUITS_360_TEST_DATASET

@algo image_classifier dataset review - .

@upload public,zip .
@assets publish \
    extensions=png,push .
```


![image](../../../../../assets/fruits-365-dataset-2025-07-01-gn9up7/grid.png?raw=true)

[fruits-365-dataset-2025-07-01-gn9up7.tar.gz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/fruits-365-dataset-2025-07-01-gn9up7.tar.gz)

```yaml
dataset:
  class_count: 3
  classes:
    0: Apple 8
    1: Blackberrie 2
    2: Cherry Wax Red 1
  count: 99
  ratios:
    eval: 0.09999999999999998
    test: 0.1
    train: 0.8
  shape:
  - 100
  - 100
  - 3
  source: fruits_360
  subsets:
    eval: 11
    test: 5
    train: 83

```
