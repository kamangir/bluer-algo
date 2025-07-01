# [image classifier](./image-classifier.md): model: train

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


![image](https://github.com/kamangir/assets/blob/main/fruits-365-model-2025-07-01-1xx7hl/loss.png?raw=true)

[fruits-365-model-2025-07-01-1xx7hl](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/fruits-365-model-2025-07-01-1xx7hl.tar.gz)

```yaml
model:
  evaluation:
    eval_accuracy: 0.8181818181818182
  inputs:
    batch_size: 16
    num_epochs: 10
  training:
    loss:
    - 1.0977213124194778
    - 1.0572264101131852
    - 1.0020845467785755
    - 0.9194808185818684
    - 0.8026711258543543
    - 0.6851499109383089
    - 0.5528762584709259
    - 0.488377235201468
    - 0.451668375945953
    - 0.45595045190259637

```
