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
    eval_accuracy: 0.9090909090909091
  inputs:
    batch_size: 16
    num_epochs: 10
  training:
    loss:
    - 1.0964517148144275
    - 1.0774549102208701
    - 1.0508584703307553
    - 1.0059286434966397
    - 0.9583562713071524
    - 0.8883721002613205
    - 0.7515504180666912
    - 0.6100954557039652
    - 0.5183466507727841
    - 0.46211635994623945

```
