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


![image](https://github.com/kamangir/assets/blob/main/fruits-365-model-2025-07-01-10jcvz/loss.png?raw=true)

[fruits-365-model-2025-07-01-10jcvz](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/fruits-365-model-2025-07-01-10jcvz.tar.gz)

```yaml
model:
  evaluation:
    eval_accuracy: 0.8181818181818182
  inputs:
    batch_size: 16
    num_epochs: 10
  training:
    loss:
    - 1.101122374994209
    - 1.0735292607043163
    - 1.047925407627979
    - 1.0089323714555027
    - 0.9721487128590963
    - 0.909971426050347
    - 0.8316032685429217
    - 0.7370915635522589
    - 0.608678322958659
    - 0.5186972697097135

```
