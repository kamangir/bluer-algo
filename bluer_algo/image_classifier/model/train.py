import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import transforms
from torch.utils.data import DataLoader
from tqdm import tqdm

from blueness import module
from bluer_objects import objects

from bluer_algo import NAME
from bluer_algo.image_classifier.dataset.classes import ImageClassifierDataset
from bluer_algo.image_classifier.model.dataset import ImageDataset
from bluer_algo.image_classifier.model.model import TinyCNN
from bluer_algo.logger import logger


NAME = module.name(__file__, NAME)


def train(
    dataset_object_name: str,
    model_object_name: str,
    batch_size: int = 16,
    num_epochs: int = 10,
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
    for epoch in range(num_epochs):
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

        logger.info(
            f"Epoch {epoch+1}, Loss: {running_loss / len(train_loader.dataset):.4f}"
        )

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

    logger.info(f"eval accuracy: {100 * correct / total:.2f}%")

    return True
