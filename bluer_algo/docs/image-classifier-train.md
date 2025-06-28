# [image classifier](./image-classifier.md): train

uses [ingest](./image-classifier-ingest.md).

```bash
@select fruits-365-dataset-2025-06-28-rtpost
@select fruits-365-model-$(@@timestamp)

🔥

@algo image_classifier train \
    TBA .. .

@upload filename=metadata.yaml .
@upload public,zip .
@assets publish \
    extensions=png,push .
```


![image](https://github.com/kamangir/assets/blob/main/TBA/grid.png?raw=true)

[TBA](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/TBA.tar.gz)

```yaml
{}

```
