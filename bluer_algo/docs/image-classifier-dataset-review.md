# [image classifier](./image-classifier.md): dataset: review

🔥

uses [ingest](./image-classifier-dataset-ingest.md).

```bash
@select $BLUER_ALGO_FRUITS_360_TEST_DATASET

@algo image_classifier dataset review \
    ~download .

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
