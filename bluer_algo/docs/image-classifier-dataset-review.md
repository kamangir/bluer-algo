# [image classifier](./image-classifier.md): dataset: review

uses [ingest](./image-classifier-dataset-ingest.md).

```bash
@select $BLUER_ALGO_FRUITS_360_TEST_DATASET

@algo image_classifier dataset review - .

@assets publish \
    extensions=png,push .
```


![image](https://github.com/kamangir/assets/blob/main/fruits-365-dataset-2025-07-01-gn9up7/grid.png?raw=true)
