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


![image](https://github.com/kamangir/assets/blob/main/fruits-365-model-2000-2025-07-01-9ulpt0/loss.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/fruits-365-model-2000-2025-07-01-9ulpt0/evaluation.png?raw=true)

![image](https://github.com/kamangir/assets/blob/main/fruits-365-model-2000-2025-07-01-9ulpt0/confusion_matrix.png?raw=true)

[fruits-365-model-2000-2025-07-01-9ulpt0](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/fruits-365-model-2000-2025-07-01-9ulpt0.tar.gz)

```yaml
model:
  dataset:
    class_count: 3
    classes:
      0: Carrot 1
      1: Pepper Orange 1
      2: Pineapple 1
    count: 1343
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
    - 0.8873637249342392
    - 0.18658611598060637
    - 0.006628601441304736
    - 0.0009866195534257308
    - 0.0003038052316308161
    - 0.0001323516886700848
    - 7.443356490224833e-05
    - 4.8406909770574926e-05
    - 3.372730305958171e-05
    - 2.5084202065430525e-05

```
