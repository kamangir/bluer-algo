from typing import Dict, Any
from ultralytics import YOLO

from blueness import module
from bluer_objects.metadata import post_to_object

from bluer_algo import NAME
from bluer_algo.logger import logger


NAME = module.name(__file__, NAME)


def train(
    dataset_object_name: str,
    model_object_name: str,
    epochs: int = 30,
    imgsz: int = 640,
    batch: int = 8,
    from_scratch: bool = False,
    validate: bool = True,
) -> bool:
    metadata: Dict[str, Any] = {}

    logger.info(
        "{}.train: {} -{}-epochs-{}-pixels-{}-batch:{}-{}> {}".format(
            NAME,
            dataset_object_name,
            epochs,
            imgsz,
            batch,
            "from-scratch" if from_scratch else "transfer-learning",
            "validate-" if validate else "",
            model_object_name,
        )
    )

    if from_scratch:
        logger.info(f"training from scratch, using {args.model_yaml}")
        model = YOLO(args.model_yaml)
    else:
        logger.info(f"transfer learning, from {args.pretrained}")
        model = YOLO(args.pretrained)

    train_metrics = model.train(
        data=args.data,  # path to your coco128.yaml
        epochs=epochs,
        imgsz=imgsz,
        batch=batch,
        device=args.device,  # e.g., '0' for GPU 0 or 'cpu'
        workers=args.workers,
        project=args.project,
        name=args.name,
        verbose=True,
        seed=0,  # reproducibility (as much as possible)
        close_mosaic=10,  # a small quality bump near the end
    )
    logger.info(f"training complete, metrics: {train_metrics}")
    metadata["train"] = train_metrics

    if validate:
        logger.info("validation the best checkpoint...")

        # gives mAP, precision/recall, etc.
        val_metrics = model.val(
            data=args.data,
            imgsz=imgsz,
            device=args.device,
        )
        logger.info(
            f"validation metrics: {val_metrics}",
        )
        metadata["validation"] = val_metrics

    return post_to_object(
        model_object_name,
        "train",
        metadata,
    )
