# [image classifier](./image-classifier.md): train

uses [ingest](./image-classifier-ingest.md).

```bash
@select $BLUER_ALGO_FRUITS_360_TEST_DATASET
@select fruits-365-model-$(@@timestamp)

@algo image_classifier train \
    - .. .

🔥

@upload filename=metadata.yaml .
@upload public,zip .
@assets publish \
    extensions=png,push .
```


![image](https://github.com/kamangir/assets/blob/main/env?raw=true)

[env](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/env.tar.gz)

```yaml
{}

```
