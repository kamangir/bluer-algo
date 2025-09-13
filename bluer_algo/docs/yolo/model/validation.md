# yolo: model: validation

## ingest

```bash
@select coco128-$(@@timestamp)

@yolo dataset ingest - . \
    --classes person

@yolo dataset review \
    ~download .

@assets publish \
    extensions=png,push .
```


![image](https://github.com/kamangir/assets/blob/main/coco128-2025-09-13-v7pmdb/review.png?raw=true)

```yaml
dataset:
  count: 61
names:
  0: person
path: ./coco128
source: coco_128
train: images/train2017
val: images/train2017

```

## train

```bash
@select coco128-model-$(@@timestamp)

@yolo model train \
    ~download .. . \
    --epochs 20

@upload public,zip .

@assets publish \
    extensions=jpg+png . \
    --prefix train/

@assets publish \
    extensions=jpg+png,push . \
    --prefix validation/
```


[coco128-model-2025-09-13-byb8uq](https://kamangir-public.s3.ir-thr-at1.arvanstorage.ir/coco128-model-2025-09-13-byb8uq.tar.gz)

| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-13-byb8uq/labels.jpg?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-13-byb8uq/results.png?raw=true) |

| | | | |
|-|-|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-13-byb8uq/BoxF1_curve.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-13-byb8uq/BoxPR_curve.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-13-byb8uq/BoxP_curve.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-13-byb8uq/BoxR_curve.png?raw=true) |

| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-13-byb8uq/confusion_matrix.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-13-byb8uq/confusion_matrix_normalized.png?raw=true) |

| | | |
|-|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-13-byb8uq/train_batch0.jpg?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-13-byb8uq/train_batch1.jpg?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-13-byb8uq/train_batch2.jpg?raw=true) |

| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-13-byb8uq/val_batch0_labels.jpg?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-13-byb8uq/val_batch0_pred.jpg?raw=true) |
| ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-13-byb8uq/val_batch1_labels.jpg?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-13-byb8uq/val_batch1_pred.jpg?raw=true) |
| ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-13-byb8uq/val_batch2_labels.jpg?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/coco128-model-2025-09-13-byb8uq/val_batch2_pred.jpg?raw=true) | 

```yaml
{}

```


## predict

```bash
🚧
```
