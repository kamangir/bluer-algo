# aliases: yolo

## dataset

```bash
@yolo \
	dataset \
	ingest \
	[dryrun,source=coco_128,upload] \
	[-|<object-name>]
 . ingest -> <object-name>.
@yolo \
	dataset \
	review \
	[~download,upload] \
	[.|<object-name>]
 . review <object-name>.
```
