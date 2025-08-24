import argparse

from blueness import module
from blueness.argparse.generic import sys_exit

from bluer_algo import NAME
from bluer_algo.yolo.model.train import train
from bluer_algo.logger import logger

NAME = module.name(__file__, NAME)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="train",
)
parser.add_argument(
    "--dataset_object_name",
    type=str,
)
parser.add_argument(
    "--model_object_name",
    type=str,
)
parser.add_argument(
    "--epochs",
    type=int,
    default=30,
    help="Number of training epochs",
)
parser.add_argument(
    "--imgsz",
    type=int,
    default=640,
    help="Training image size",
)
parser.add_argument(
    "--batch",
    type=int,
    default=8,
    help="Batch size (adjust to your VRAM/CPU)",
)

# review v 🔥


parser.add_argument(
    "--data",
    required=True,
    type=str,
    help="Path to data YAML (e.g., coco128.yaml). Must contain train/val paths.",
)
parser.add_argument(
    "--device",
    type=str,
    default=None,
    help="Device string for PyTorch (e.g., '0', '0,1', 'cpu'). None = auto",
)
parser.add_argument(
    "--workers",
    type=int,
    default=4,
    help="Dataloader workers (Windows users: try 0 if you hit issues)",
)
parser.add_argument(
    "--project",
    type=str,
    default="runs/train",
    help="Project folder",
)
parser.add_argument(
    "--name",
    type=str,
    default="yolov8n-coco128",
    help="Run name",
)
parser.add_argument(
    "--pretrained",
    type=str,
    default="yolov8n.pt",
    help="Pretrained weights to start from ('.pt'). Ignored if --scratch.",
)
parser.add_argument(
    "--model_yaml",
    type=str,
    default="yolov8n.yaml",
    help="Model YAML when training from scratch (e.g., yolov8n.yaml, yolov8s.yaml).",
)

# review ^ 🔥

parser.add_argument(
    "--from_scratch",
    type=int,
    default=0,
    help="0 | 1: Train from scratch (use a model YAML, no Internet needed).",
)
parser.add_argument(
    "--validate",
    type=int,
    default=1,
    help="0 | 1: run validation after training",
)

args = parser.parse_args()

success = False
if args.task == "train":
    success = train(
        dataset_object_name=args.dataset_object_name,
        model_object_name=args.model_object_name,
        epochs=args.epochs,
        imgsz=args.imgsz,
        batch=args.batch,
        from_scratch=args.from_scratch == 1,
        validate=args.validate == 1,
    )
else:
    success = None

sys_exit(logger, NAME, args.task, success)
