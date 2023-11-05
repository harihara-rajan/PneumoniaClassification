from constants.__init__ import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from entity.entity_config import DataIngestionEntity
from utils.common import read_yaml, create_dirs
from pathlib import Path
class ConfigurationManager:
    def __init__(self, config_path=CONFIG_FILE_PATH, params_path=PARAMS_FILE_PATH):
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)
    def get_data_ingestion_entity(self)-> DataIngestionEntity:
        config = self.config.data_ingestion
        die = DataIngestionEntity(
            url=config.url,
            root_dir_zip=config.root_dir_zip,
            root_dir=config.root_dir
        )
        return die

if __name__ == '__main__':
    cm = ConfigurationManager()
