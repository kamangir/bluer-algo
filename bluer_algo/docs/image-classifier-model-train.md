# [image classifier](./image-classifier.md): model: train

uses [ingest](./image-classifier-dataset-ingest.md).

```bash
@select $BLUER_ALGO_FRUITS_360_TEST_DATASET
@select fruits-365-model-$(@@timestamp)

@algo image_classifier model train \
    ~download,upload .. .

@upload public,zip .
@assets publish \
    extensions=png,push .
```


![image](https://github.com/kamangir/assets/blob/main/fruits-365-model-2025-07-01-9wm886/loss.png?raw=true)

[fruits-365-model-2025-07-01-9wm886](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/fruits-365-model-2025-07-01-9wm886.tar.gz)

```yaml
model:
  dataset:
    class_count: 3
    classes:
      0: Apple 8
      1: Blackberrie 2
      2: Cherry Wax Red 1
    count: 99
    shape:
    - 100
    - 100
    - 3
  evaluation:
    eval_accuracy: 0.6363636363636364
  inputs:
    batch_size: 16
    num_epochs: 10
  training:
    loss:
    - 1.0935780930231853
    - 1.0560941782342381
    - 0.9956620285309941
    - 0.9361136189426285
    - 0.8835492313626301
    - 0.778554870421628
    - 0.6616675702922316
    - 0.578948836728751
    - 0.505560634366001
    - 0.4718829784766737

```
