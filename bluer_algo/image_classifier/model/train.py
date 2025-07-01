import torch
from torch import nn
from torch import optim
from torchvision import transforms
from torch.utils.data import DataLoader
from tqdm import tqdm, trange
from typing import List
import matplotlib.pyplot as plt

from blueness import module
from bluer_objects import objects
from bluer_objects.metadata import post_to_object
from bluer_objects import file
from bluer_objects.graphics.signature import justify_text

from bluer_algo import NAME
from bluer_algo.host import signature
from bluer_algo.image_classifier.dataset.dataset import ImageClassifierDataset
from bluer_algo.image_classifier.model.dataset import ImageDataset
from bluer_algo.image_classifier.model.model import TinyCNN
from bluer_algo.logger import logger


NAME = module.name(__file__, NAME)


def train(
    dataset_object_name: str,
    model_object_name: str,
    batch_size: int = 16,
    num_epochs: int = 10,
    log: bool = True,
    verbose: bool = False,
    line_width: int = 80,
) -> bool:
    logger.info(
        "{}.train: {} -> {}".format(
            NAME,
            dataset_object_name,
            model_object_name,
        )
    )

    success, dataset = ImageClassifierDataset.load(
        object_name=dataset_object_name,
    )
    if not success:
        return success

    object_path = objects.object_path(
        object_name=dataset.object_name,
    )
    num_workers = 2 if torch.cuda.is_available() else 0
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    transform = transforms.Compose(
        [
            transforms.Resize((100, 100)),
            transforms.ToTensor(),
        ]
    )

    train_df = dataset.df[dataset.df["subset"] == "train"]
    eval_df = dataset.df[dataset.df["subset"] == "eval"]

    train_set = ImageDataset(train_df, object_path, transform)
    eval_set = ImageDataset(eval_df, object_path, transform)

    train_loader = DataLoader(
        train_set, batch_size=batch_size, shuffle=True, num_workers=num_workers
    )
    eval_loader = DataLoader(
        eval_set, batch_size=batch_size, shuffle=False, num_workers=num_workers
    )

    model = TinyCNN(num_classes=dataset.class_count).to(device)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    logger.info("training...")
    epoch_loss_list: List[float] = []
    for epoch in trange(num_epochs):
        model.train()
        running_loss = 0.0
        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)

            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item() * images.size(0)

        epoch_loss = float(running_loss / len(train_loader.dataset))
        epoch_loss_list.append(epoch_loss)
        logger.info(f"epoch #{epoch+1}, loss: {epoch_loss:.4f}")

    logger.info("evaluating...")
    model.eval()
    correct = total = 0
    with torch.no_grad():
        for images, labels in tqdm(eval_loader):
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    eval_accuracy = correct / total
    logger.info(f"eval accuracy: {100 * eval_accuracy:.2f}%")

    # plotting
    plt.figure(figsize=(10, 5))
    plt.plot(
        range(num_epochs),
        epoch_loss_list,
        marker="o",
    )
    plt.title("Epoch Loss")
    plt.xlabel(
        justify_text(
            " | ".join(["Epoch"] + signature()),
            line_width=line_width,
            return_str=True,
        )
    )
    plt.ylabel("Loss")
    plt.title(
        justify_text(
            " | ".join(
                objects.signature(object_name=dataset_object_name)
                + dataset.signature()
                + [
                    f"batch_size: {batch_size}",
                    f"num_epochs: {num_epochs}",
                    f"eval_accuracy: {100*eval_accuracy:.2f}%",
                ]
            ),
            line_width=line_width,
            return_str=True,
        )
    )
    plt.grid(True)
    if not file.save_fig(
        objects.path_of(
            object_name=model_object_name,
            filename="loss.png",
        ),
        log=log,
    ):
        return False

    return post_to_object(
        object_name=model_object_name,
        key="model",
        value={
            "dataset": {
                "count": dataset.count,
                "classes": dataset.dict_of_classes,
                "class_count": dataset.class_count,
                "shape": dataset.shape,
            },
            "inputs": {
                "batch_size": batch_size,
                "num_epochs": num_epochs,
            },
            "training": {
                "loss": epoch_loss_list,
            },
            "evaluation": {
                "eval_accuracy": eval_accuracy,
            },
        },
    )
