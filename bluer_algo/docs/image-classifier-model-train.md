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

![image](https://github.com/kamangir/assets/blob/main/fruits-365-model-2025-07-01-9wm886/evaluation.png?raw=true)

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
    - 1.0965443964464119
    - 1.0777758460447013
    - 1.0312952937850033
    - 0.9516922235488892
    - 0.8368437153747282
    - 0.6827004510595138
    - 0.5461112695286073
    - 0.48642386657645903
    - 0.44807900937206774
    - 0.423772053187152

```
