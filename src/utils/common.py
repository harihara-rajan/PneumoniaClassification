import os
import yaml 
from pathlib import Path
from box import ConfigBox
def read_yaml(path_to_yamlfile:Path)-> ConfigBox:
    with open(path_to_yamlfile) as yaml_file:
        content =yaml.safe_load(yaml_file)
    return ConfigBox(content)

def create_dirs(list_dirs:list)-> None:

    for dir in list_dirs:
        if not os.path.exists(dir):
            os.makedirs(dir, exist_ok=True)


if __name__ == '__main__':
    configbox = read_yaml(Path("E:\PneumoniaClassification\src\yaml\config.yaml"))
    test_key = configbox.test_key
    print(test_key.test_key1)
    print(test_key.test_key2)
    print(test_key.test_key3)
