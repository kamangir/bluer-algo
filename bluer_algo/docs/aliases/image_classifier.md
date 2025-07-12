# image_classifier

## dataset

```bash
@image_classifier \
	dataset \
	ingest \
	[clone,count=<100>,source=fruits_360,upload] \
	[-|<object-name>] \
	[--class_count -1] \
	[--test_ratio 0.1] \
	[--train_ratio 0.8]
 . ingest -> <object-name>.
@image_classifier \
	dataset \
	review \
	[~download,upload] \
	[.|<object-name>]
 . review <object-name>.
@image_classifier \
	dataset \
	sequence \
	[~download,length=<2>,upload] \
	[.|<source-object-name>] \
	[-|<destination-object-name>]
 . <source-object-name> -sequence-> <destination-object-name>.
```

## model

```bash
@image_classifier \
	model \
	prediction_test \
	[~download,upload] \
	[..|<dataset-object-name>] \
	[.|<model-object-name>] \
	[-|<prediction-object-name>]
 . test prediction.
@image_classifier \
	model \
	train \
	[~download,upload] \
	[.|<dataset-object-name>] \
	[-|<model-object-name>] \
	[--batch_size 16] \
	[--num_epochs 10]
 . <dataset-object-name> -train-> <model-object-name>.
```
