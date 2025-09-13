# image-classifier: model: train: large

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
