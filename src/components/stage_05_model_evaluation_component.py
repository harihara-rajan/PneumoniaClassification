import os
from config.configuration import ModelEvaluationEntity
import tensorflow as tf
from pathlib import Path
from utils.common import save_json

class ModelEvaluation:
    def __init__(self, ModelEvaluationEntity):
        self.config = ModelEvaluationEntity
    
    def _valid_generator(self):
        data_preprocessing_kwargs = dict(
            rescale=1./255, 
            validation_split = 0.3
        )
        valid_data_preprocessing = tf.keras.preprocessing.image.ImageDataGenerator(**data_preprocessing_kwargs)
        self.valid_data_generator  = valid_data_preprocessing.flow_from_directory(
            directory = self.config.training_data_path, 
            target_size= self.config.params_image_size[:-1],
            batch_size= self.config.params_batch_size, 
            shuffle=False
        )
    
    @property
    def _load_model(path:Path):  
        print(path)
        return tf.keras.models.load_model(path)
    
    def evaluation(self):
        # self.model = self._load_model(self.config.trained_model_path)
        model = tf.keras.models.load_model(self.config.trained_model_path)
        self._valid_generator()
        self.score = model.evaluate(self.valid_data_generator) # list ["loss", "acc"]
    
    def save_score(self):
        scores = dict(
            loss = self.score[0],
            accuracy = self.score[1]
        )
        save_json(values= scores, 
                  path=os.path.join(os.path.dirname(self.config.trained_model_path),"training_score.json"))
        

