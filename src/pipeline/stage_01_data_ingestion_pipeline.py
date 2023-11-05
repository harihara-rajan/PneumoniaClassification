import os
from config.configuration import ConfigurationManager

class DataIngestionPipeline:
    def __init__(self):
        pass
    def main():
        cm = ConfigurationManager()
        DataIngestionEntity = cm.get_data_ingestion_entity()
        DataIngestionComponent = DataIngestionComponent(DataIngestionEntity)
        DataIngestionComponent.download_data()
        DataIngestionComponent.extract_data()

if __name__ == "__main__":
    obj = DataIngestionPipeline()
    obj.main()
