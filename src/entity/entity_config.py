from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionEntity:
    url: str
    root_dir_zip:Path
    root_dir: Path

@dataclass(frozen=True)
class BaseModelGeneratorEntity:
    base_model_path : Path
    actual_model_path : Path
    CLASSES: int 
    EPOCHS: int
    BATCH_SIZE: int
    LR: float
    TEST_SIZE: float
    IMAGE_SIZE: list