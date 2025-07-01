# [image classifier](./image-classifier.md): model: train

## small dataset

uses [ingest](./image-classifier-dataset-ingest.md).

```bash
@select $BLUER_ALGO_FRUITS_360_TEST_DATASET
@select fruits-365-model-$(@@timestamp)

@algo image_classifier model train \
    upload .. .

@upload public,zip .
@assets publish \
    extensions=png,push .
```


![image](https://github.com/kamangir/assets/blob/main/fruits-365-model-2025-07-01-ltzxw0/loss.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/fruits-365-model-2025-07-01-ltzxw0/evaluation.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/fruits-365-model-2025-07-01-ltzxw0/confusion_matrix.png?raw=true)

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

## large dataset

```bash
@select fruits-365-dataset-2000-$(@@timestamp)

@algo image_classifier dataset ingest \
    clone,count=10000,source=fruits_360 . \
    --class_count 3

@select fruits-365-model-2000-$(@@timestamp)

@algo image_classifier model train \
    ~download,upload .. .

@upload public,zip .
@assets publish \
    extensions=png,push .
```


![image](https://github.com/kamangir/assets/blob/main//loss.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main//evaluation.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main//confusion_matrix.png?raw=true)

[](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/.tar.gz)

```yaml
api_count: 2167
created_by: bluer_geo-5.15.1-bluer_flow-5.16.1-bluer_ai-12.136.1-bluer_objects-6.96.1-bluer_options-5.86.1-torch-2.2.2-Python
  3.12.9-Darwin 23.6.0--Jupyter-Notebook
creation_date: 23 April 2025, 10:33:49
dataset:
  class_count: 10
  classes:
    0: Apple 8
    1: Apple Braeburn 1
    2: Apple Golden 1
    3: Apple hit 1
    4: Cactus fruit red 1
    5: Cherry 4
    6: Nut 3
    7: Pear Red 1
    8: Tomato Cherry Orange 1
    9: Zucchini 1
  count: 10
  ratios:
    eval: 0.09999999999999998
    test: 0.1
    train: 0.8
  source: fruits_360
  subsets:
    eval: 2
    test: 0
    train: 8
description: Civilian Harm in Ukraine TimeMap
failure_count: 0
ingested_count: 2167
range:
- 2022-02-24
- 2025-04-06

```
