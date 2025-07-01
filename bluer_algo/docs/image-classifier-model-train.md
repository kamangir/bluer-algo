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


![image](https://github.com/kamangir/assets/blob/main/fruits-365-model-2025-07-01-ltzxw0/loss.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/fruits-365-model-2025-07-01-ltzxw0/evaluation.png?raw=true)

[fruits-365-model-2025-07-01-ltzxw0](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/fruits-365-model-2025-07-01-ltzxw0.tar.gz)

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
    - 1.0920882842626916
    - 1.0682448723230018
    - 1.024236264717148
    - 0.9647200509726283
    - 0.8594309630164181
    - 0.7342140818216715
    - 0.6408237829265824
    - 0.5509795618344502
    - 0.502587627933686
    - 0.47540893396699285

```
