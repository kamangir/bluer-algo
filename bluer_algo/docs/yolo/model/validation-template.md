title:::

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

set:::dataset_object_name coco128-2025-09-15-6rpxu2

object:::get:::dataset_object_name

assets:::get:::dataset_object_name/review.png

metadata:::get:::dataset_object_name

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

set:::model_object_name env:::BLUER_ALGO_COCO128_TEST_MODEL

object:::get:::model_object_name

| | |
|-|-|
| assets:::get:::model_object_name/labels.jpg | assets:::get:::model_object_name/results.png |

| | | | |
|-|-|-|-|
| assets:::get:::model_object_name/BoxF1_curve.png | assets:::get:::model_object_name/BoxPR_curve.png | assets:::get:::model_object_name/BoxP_curve.png | assets:::get:::model_object_name/BoxR_curve.png |

| | |
|-|-|
| assets:::get:::model_object_name/confusion_matrix.png | assets:::get:::model_object_name/confusion_matrix_normalized.png |

| | | |
|-|-|-|
| assets:::get:::model_object_name/train_batch0.jpg | assets:::get:::model_object_name/train_batch1.jpg | assets:::get:::model_object_name/train_batch2.jpg |

| | |
|-|-|
| assets:::get:::model_object_name/val_batch0_labels.jpg | assets:::get:::model_object_name/val_batch0_pred.jpg |
| assets:::get:::model_object_name/val_batch1_labels.jpg | assets:::get:::model_object_name/val_batch1_pred.jpg |
| assets:::get:::model_object_name/val_batch2_labels.jpg | assets:::get:::model_object_name/val_batch2_pred.jpg | 

details:::metadata
metadata:::get:::model_object_name
details:::

## predict

```bash
🚧
```