# aliases: yolo

## dataset

```bash
@yolo \
	dataset \
	ingest \
	[dryrun,source=coco_128,upload] \
	[-|<object-name>] \
	[--classes all | person+boat] \
	[--verbose 1]
 . ingest -> <object-name>.
@yolo \
	dataset \
	review \
	[~download,upload] \
	[.|<object-name>] \
	[--verbose 1]
 . review <object-name>.
```

## model

```bash
@yolo \
	model \
	prediction_test \
	[~download,upload] \
	[..|<dataset-object-name>] \
	[.|<model-object-name>] \
	[-|<prediction-object-name>]
 . test prediction.
@yolo \
	model \
	train \
	[~download,upload] \
	[.|<dataset-object-name>] \
	[-|<model-object-name>] \
	[--batch 8] \
	[--device cpu | 0 | 0,1] \
	[--epochs 30] \
	[--from_scratch 1] \
	[--image_size 640] \
	[--model_size nano | small | medium | large | xlarge] \
	[--validate 0] \
	[--verbose 1] \
	[--workers 4]
 . train.
```
