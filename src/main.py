from config.configuration import ConfigurationManager
from components.stage_01_data_ingestion import DataIngestionComponent
from constants.__init__ import CONFIG_FILE_PATH, CONFIG_FILE_PATH
# import os
# stage01= "Data Ingestion"

try:
    cm = ConfigurationManager()
    die = cm.get_data_ingestion_entity()
    DataIngestionComponent = DataIngestionComponent(die)
    DataIngestionComponent.download_data()
    DataIngestionComponent.extract_data()
except Exception as e:
    raise e