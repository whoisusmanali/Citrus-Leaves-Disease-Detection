
import os
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

NUM_WORKERS = os.cpu_count()

def create_dataloaders(
    train_dir: str,
    valid_dir: str,
    train_transform: transforms.Compose,
    valid_transform: transforms.Compose,
    batch_size: int,
    num_workers: int=NUM_WORKERS
):
  # Use ImageFolder to create datasets(s)
  train_data = datasets.ImageFolder(train_dir, transform=train_transform)
  valid_data = datasets.ImageFolder(valid_dir, transform=valid_transform)

  # Get class names
  class_names = train_data.classes

  # Turn images into dataloaders
  train_dataloader = DataLoader(
      train_data,
      batch_size=batch_size,
      shuffle=True,
      num_workers=num_workers,
      pin_memory=True
  )
  valid_dataloader = DataLoader(
      valid_data,
      batch_size=batch_size,
      shuffle=False,
      num_workers=num_workers,
      pin_memory=True
  )

  return train_dataloader, valid_dataloader, class_names
  
