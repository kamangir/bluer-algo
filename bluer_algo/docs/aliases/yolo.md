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
