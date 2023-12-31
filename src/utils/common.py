import os
import yaml
from pathlib import Path
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
import json
# @ensure_annotations
def read_yaml(path_to_yamlfile)-> ConfigBox:
    with open(path_to_yamlfile,'r') as yaml_file:
        content = yaml.safe_load(yaml_file)
        return ConfigBox(content)
# @ensure_annotations
def create_dirs(list_dirs:list[str])-> None:
    for dir in list_dirs:
        if not os.path.exists(dir):
            os.makedirs(dir, exist_ok=True)

def save_json(values:dict, path:Path)-> None:
    with open(path, 'w') as json_file:
        json.dump(values, json_file)

if __name__ == '__main__':
    configbox = read_yaml(Path("E:\PneumoniaClassification\src\yml\config.yaml"))
    test_key = configbox.base_model_generator
    print(test_key.base_model_path)
    print(test_key.actual_model_path)