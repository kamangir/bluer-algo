# [image classifier](../): Model: Train

## small dataset

uses [ingest](../image_classifier/ingest.md).

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


![image](https://github.com/kamangir/assets/blob/main/fruits-365-model-2000-2025-07-02-k318ju/loss.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/fruits-365-model-2000-2025-07-02-k318ju/evaluation.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/fruits-365-model-2000-2025-07-02-k318ju/confusion_matrix.png?raw=true)

[fruits-365-model-2000-2025-07-02-k318ju](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/fruits-365-model-2000-2025-07-02-k318ju.tar.gz)

```yaml
model:
  dataset:
    class_count: 3
    classes:
      0: Lychee 1
      1: Pear Forelle 1
      2: Physalis with Husk 1
    count: 1684
    shape:
    - 100
    - 100
    - 3
  evaluation:
    class_accuracy:
      0: 1.0
      1: 1.0
      2: 1.0
    eval_accuracy: 1.0
  inputs:
    batch_size: 16
    num_epochs: 10
  training:
    loss:
    - 0.7043376307912738
    - 0.08943271208881286
    - 0.008551867894572343
    - 0.004447948475223993
    - 0.0016600372687074743
    - 0.0010692106054555244
    - 0.0008688547763543214
    - 0.0006009176277234873
    - 0.0004981696757456296
    - 0.0004295692094449789

```
