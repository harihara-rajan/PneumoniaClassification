import os
import logging
import zipfile
import requests
from utils.common import read_yaml, create_dirs
from entity.entity_config import DataIngestionEntity
logging.basicConfig(level=logging.INFO, format='%(message)s')
class DataIngestionComponent:
    def __init__(self, DataIngestionEntity):
        self.config = DataIngestionEntity
    
    def download_data(self)-> None:     
        response = requests.get(self.config.url)
        self.filename = os.path.basename(self.config.url)
        create_dirs([self.config.root_dir_zip])
        fname = os.path.join(self.config.root_dir_zip, self.filename)
        if response.status_code == 200:
            with open(fname, 'wb') as f:
                f.write(response.content)
                logging.info("Data downloaded successfully")
    
    def extract_data(self)-> None:
        create_dirs([self.config.root_dir])
        path_to_zip_file = os.path.join(self.config.root_dir_zip,self.filename)
        zipfile.ZipFile(path_to_zip_file).extractall(self.config.root_dir)
