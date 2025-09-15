# image-classifier: model: train: small

uses [ingest](../../dataset/ingest.md).

```bash
@select $BLUER_ALGO_FRUITS_360_TEST_DATASET
@select fruits-365-model-$(@@timestamp)

@algo image_classifier model train \
    upload .. .

@upload public,zip .
@assets publish \
    extensions=png,push .
```


![image](https://github.com/kamangir/assets/blob/main/fruits-365-model-2025-07-02-fvfomt/loss.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/fruits-365-model-2025-07-02-fvfomt/evaluation.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/fruits-365-model-2025-07-02-fvfomt/confusion_matrix.png?raw=true)

[fruits-365-model-2025-07-02-fvfomt](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/fruits-365-model-2025-07-02-fvfomt.tar.gz)

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
    class_accuracy:
      0: 1.0
      1: 1.0
      2: 0.75
    eval_accuracy: 0.9090909090909091
  inputs:
    batch_size: 16
    num_epochs: 10
  training:
    loss:
    - 1.1059847007314842
    - 1.0944474734455707
    - 1.081830551825374
    - 1.0557171982454967
    - 1.0102007518331688
    - 0.9688218681209059
    - 0.9016210835382162
    - 0.7881300334470818
    - 0.6774013846753592
    - 0.5369924443313875

```
