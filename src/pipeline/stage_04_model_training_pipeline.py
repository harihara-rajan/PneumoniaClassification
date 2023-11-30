import os 
from config.configuration import ConfigurationManager
from components.stage_03_callbacks import CALLBACKSCOMPONENT
from components.stage_04_model_training import TrainingComponent
from constants.__init__ import PARAMS_FILE_PATH, CONFIG_FILE_PATH
from utils.common import read_yaml

class ModelTrainingPipeline():
    def __init__(self, params_path = PARAMS_FILE_PATH, config_path=CONFIG_FILE_PATH):
        self.params = read_yaml(params_path)
        self.config = read_yaml(config_path)
    
    def main():
        cm = ConfigurationManager()
        callbacksentity = cm.get_callbacks_entity()
        callbacks_component = CALLBACKSCOMPONENT(callbacksentity)
        callback = callbacks_component.callbacks_list()

        training_entity = cm.get_training_entity()
        training_component = TrainingComponent(TrainingEntity= training_entity)
        training_component.test_train_split()
        training_component.train(callback_list=callback)
    