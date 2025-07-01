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


![image](https://github.com/kamangir/assets/blob/main/fruits-365-model-2025-07-01-g0ffa9/loss.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/fruits-365-model-2025-07-01-g0ffa9/evaluation.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/fruits-365-model-2025-07-01-g0ffa9/confusion_matrix.png?raw=true)

[fruits-365-model-2025-07-01-g0ffa9](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/fruits-365-model-2025-07-01-g0ffa9.tar.gz)

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
      0: 0.6666666666666666
      1: 1.0
      2: 1.0
    eval_accuracy: 0.9090909090909091
  inputs:
    batch_size: 16
    num_epochs: 10
  training:
    loss:
    - 1.0955626404429057
    - 1.065239673637482
    - 1.0129518164209572
    - 0.9348489347710667
    - 0.8087216572589185
    - 0.6532617714031633
    - 0.5209052735064403
    - 0.46322603038994664
    - 0.4511759938245796
    - 0.39809396468013164

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


![image](https://github.com/kamangir/assets/blob/main/fruits-365-model-2000-2025-07-01-0f5c3i/loss.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/fruits-365-model-2000-2025-07-01-0f5c3i/evaluation.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/fruits-365-model-2000-2025-07-01-0f5c3i/confusion_matrix.png?raw=true)

[fruits-365-model-2000-2025-07-01-0f5c3i](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/fruits-365-model-2000-2025-07-01-0f5c3i.tar.gz)

```yaml
model:
  dataset:
    class_count: 3
    classes:
      0: Apple Red Yellow 1
      1: Dates 1
      2: Fig 1
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
    - 0.7802977863950497
    - 0.4736495371038071
    - 0.4408162122659987
    - 0.38462256806439343
    - 0.2753883281527978
    - 0.1924491258485835
    - 0.11263275718118987
    - 0.07249000640082041
    - 0.043517076016664005
    - 0.03726826709666855

```
