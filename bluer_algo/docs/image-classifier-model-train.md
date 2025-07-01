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


![image](https://github.com/kamangir/assets/blob/main/fruits-365-model-2025-07-01-1xx7hl/loss.png?raw=true)

[fruits-365-model-2025-07-01-1xx7hl](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/fruits-365-model-2025-07-01-1xx7hl.tar.gz)

```yaml
model:
  evaluation:
    eval_accuracy: 1.0
  inputs:
    batch_size: 16
    num_epochs: 10
  training:
    loss:
    - 1.1087961972477924
    - 1.0843626777809787
    - 1.054258179951863
    - 1.0159300307193435
    - 0.9257770791111222
    - 0.8263094008687031
    - 0.6913913912083729
    - 0.5560306870793722
    - 0.478118322699903
    - 0.3973728978490255

```
