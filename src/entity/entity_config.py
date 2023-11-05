from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionEntity:
    url: str
    root_dir_zip:Path
    root_dir: Path