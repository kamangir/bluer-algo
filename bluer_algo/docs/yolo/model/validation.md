# yolo: model: validation

## ingest

```bash
@select coco128-$(@@timestamp)

@yolo dataset ingest - . \
    --classes person

@yolo dataset review \
    ~download .

@upload public,zip

@assets publish \
    extensions=png,push .
```


[coco128-2025-09-15-6rpxu2](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/coco128-2025-09-15-6rpxu2.tar.gz)

![image](https://github.com/kamangir/assets/blob/main/coco128-2025-09-15-6rpxu2/review.png?raw=true)

```yaml
dataset:
  count: 61
names:
  0: person
source: coco_128
train: coco128/images/train2017
val: coco128/images/train2017

```

## train

```bash
@select coco128-model-$(@@timestamp)

@yolo model train \
    ~download .. . \
    --epochs 20

@upload public,zip

@assets publish \
    extensions=jpg+png . \
    --prefix train/

@assets publish \
    extensions=jpg+png,push . \
    --prefix validation/
```


[BLUER_ALGO_COCO128_TEST_MODEL](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/BLUER_ALGO_COCO128_TEST_MODEL.tar.gz)

| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/BLUER_ALGO_COCO128_TEST_MODEL/labels.jpg?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/BLUER_ALGO_COCO128_TEST_MODEL/results.png?raw=true) |

| | | | |
|-|-|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/BLUER_ALGO_COCO128_TEST_MODEL/BoxF1_curve.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/BLUER_ALGO_COCO128_TEST_MODEL/BoxPR_curve.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/BLUER_ALGO_COCO128_TEST_MODEL/BoxP_curve.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/BLUER_ALGO_COCO128_TEST_MODEL/BoxR_curve.png?raw=true) |

| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/BLUER_ALGO_COCO128_TEST_MODEL/confusion_matrix.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/BLUER_ALGO_COCO128_TEST_MODEL/confusion_matrix_normalized.png?raw=true) |

| | | |
|-|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/BLUER_ALGO_COCO128_TEST_MODEL/train_batch0.jpg?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/BLUER_ALGO_COCO128_TEST_MODEL/train_batch1.jpg?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/BLUER_ALGO_COCO128_TEST_MODEL/train_batch2.jpg?raw=true) |

| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/BLUER_ALGO_COCO128_TEST_MODEL/val_batch0_labels.jpg?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/BLUER_ALGO_COCO128_TEST_MODEL/val_batch0_pred.jpg?raw=true) |
| ![image](https://github.com/kamangir/assets/blob/main/BLUER_ALGO_COCO128_TEST_MODEL/val_batch1_labels.jpg?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/BLUER_ALGO_COCO128_TEST_MODEL/val_batch1_pred.jpg?raw=true) |
| ![image](https://github.com/kamangir/assets/blob/main/BLUER_ALGO_COCO128_TEST_MODEL/val_batch2_labels.jpg?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/BLUER_ALGO_COCO128_TEST_MODEL/val_batch2_pred.jpg?raw=true) | 


<details>
<summary>metadata</summary>

```yaml
{}

```

</details>


## predict

```bash
🚧
```
