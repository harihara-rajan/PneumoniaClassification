from constants.__init__ import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from entity.entity_config import (
                                    DataIngestionEntity, 
                                    BaseModelGeneratorEntity, 
                                    CALLBACKSENTITY, 
                                    TrainingEntity, 
                                    ModelEvaluationEntity)
from utils.common import read_yaml
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
    def get_base_model_generator_entity(self)-> BaseModelGeneratorEntity:
        
        base_model_entity = BaseModelGeneratorEntity(
            base_model_path  = self.config.base_model_generator.base_model_path,
            actual_model_path= self.config.base_model_generator.actual_model_path,
            CLASSES = self.params.CLASSES,
            EPOCHS = self.params.EPOCHS,
            BATCH_SIZE = self.params.BATCH_SIZE,
            LR = self.params.LR,
            TEST_SIZE = self.params.TEST_SIZE,
            IMAGE_SIZE = self.params.IMAGE_SIZE
        )
        return base_model_entity
    
    def get_callbacks_entity(self)->CALLBACKSENTITY :
        config = self.config.prepare_callbacks
        
        callback_entity = CALLBACKSENTITY(root_dir=config.root_dir, 
                                          tensorboard_log_dir=config.tensorboard_log_dir,
                                          checkpoint_file_path=config.checkpoint_file_path
                                          )
        return callback_entity

    def get_training_entity(self)->TrainingEntity:
        config = self.config.training
        training_entity = TrainingEntity(root_dir=config.root_dir,
                                         actual_model_path=self.config.base_model_generator.actual_model_path,
                                         trained_model_path=config.trained_model_path,
                                         training_data_path=config.training_data_path,
                                         params_epochs= self.params.EPOCHS,
                                         params_batch_size=self.params.BATCH_SIZE,
                                         params_is_augment=self.params.AUG, 
                                         params_image_size=self.params.IMAGE_SIZE,
                                         model_no=self.params.MODEL)
        return training_entity

    def get_model_evaluation_entity(self)->ModelEvaluationEntity:
        model_evaluation_entity = ModelEvaluationEntity(trained_model_path= self.config.training.trained_model_path,
            training_data_path= self.config.training.training_data_path,
            all_params= self.params,
            params_batch_size= self.params.BATCH_SIZE,
            params_image_size= self.params.IMAGE_SIZE,
            model_no=self.params.MODEL
        )
        return model_evaluation_entity

if __name__ == '__main__':
    cm = ConfigurationManager()
