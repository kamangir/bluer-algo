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


![image](https://github.com/kamangir/assets/blob/main/fruits-365-model-2025-07-02-fvfomt/loss.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/fruits-365-model-2025-07-02-fvfomt/evaluation.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/fruits-365-model-2025-07-02-fvfomt/confusion_matrix.png?raw=true)

[fruits-365-model-2025-07-02-fvfomt](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/fruits-365-model-2025-07-02-fvfomt.tar.gz)

```yaml
{}

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
{}

```
