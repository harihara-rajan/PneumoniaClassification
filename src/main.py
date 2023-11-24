from config.configuration import ConfigurationManager
from components.stage_01_data_ingestion import DataIngestionComponent
from components.stage_02_base_model_generator import BaseModelGeneratorComponent
from constants.__init__ import CONFIG_FILE_PATH, CONFIG_FILE_PATH
from pipeline.stage_02_base_model_gen_pipeline import BaseModelPipeline
# import os
stage01= "Data Ingestion"
stage02 = "Base Model Generator"

try:
    print(f"Stage 01 {stage01} stared")
    cm = ConfigurationManager()
    die = cm.get_data_ingestion_entity()
    DataIngestionComponent = DataIngestionComponent(die)
    DataIngestionComponent.download_data()
    DataIngestionComponent.extract_data()
    print(f"Stage 01 {stage01} ended")
except Exception as e:
    raise e

try:
    print(f"Stage 02 {stage02} started")
    model_gen = BaseModelPipeline()
    model_gen.main()
    print(f"Stage 02 {stage02} ended")
except Exception as e:
    raise e