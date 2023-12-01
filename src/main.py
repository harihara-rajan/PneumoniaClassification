from config.configuration import ConfigurationManager
from components.stage_01_data_ingestion import DataIngestionComponent
from components.stage_02_base_model_generator import BaseModelGeneratorComponent
from components.stage_03_callbacks import CALLBACKSCOMPONENT
from constants.__init__ import CONFIG_FILE_PATH, CONFIG_FILE_PATH
from pipeline.stage_01_data_ingestion_pipeline import DataIngestionPipeline
from pipeline.stage_02_base_model_gen_pipeline import BaseModelPipeline
# from pipeline.stage_03_callbacks_pipeline import CallBacksPipeline
from pipeline.stage_04_model_training_pipeline import ModelTrainingPipeline
from pipeline.stage_05_model_evaluation_pipeline import ModelEvaluationPipeline
# import os
stage01= "Data Ingestion"
stage02 = "Base Model Generator"
stage03 = "Model Training"
stage04 = "Model Evaluation"

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
    # di = DataIngestionPipeline
    # di.main()
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

try:
    print(f"Stage 03 {stage03} started")
    callbacks = ModelTrainingPipeline
    callbacks.main()
    print(f"Stage 03 {stage03} ended")
except Exception as e:
    raise e

try:
    print(f"Stage 04 {stage04} started")
    model_eval = ModelEvaluationPipeline
    model_eval.main()
except Exception as e:
    raise e