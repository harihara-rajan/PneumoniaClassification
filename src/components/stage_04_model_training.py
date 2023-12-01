from utils.common import create_dirs
import tensorflow as tf
import os
import pandas as pd 
class TrainingComponent():
    def __init__(self, TrainingEntity):
        self.config = TrainingEntity
        create_dirs([self.config.root_dir, os.path.dirname(self.config.trained_model_path)])
    
    # def load_model(self):

    def test_train_split(self):
        self.model = tf.keras.models.load_model(self.config.actual_model_path)
        preprocessing_kwargs = dict(
            rescale = 1./255,
            validation_split=0.2
        )

        #  generates validation data
        valid_data_gen = tf.keras.preprocessing.image.ImageDataGenerator(**preprocessing_kwargs)
        self.valid_generator = valid_data_gen.flow_from_directory( directory=self.config.training_data_path, 
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            subset='validation',
            shuffle=False
        )

        # generate training data 
        if self.config.params_is_augment:
            train_data_generator = tf.keras.preprocessing.image.ImageDataGenerator(rotation_range=40,
                                                                              horizontal_flip=True,
                                                                              width_shift_range=0.2,
                                                                              height_shift_range=0.2, 
                                                                              shear_range=0.2, 
                                                                              zoom_range=0.2,
                                                                              **preprocessing_kwargs)
        else:
            train_data_generator = valid_data_gen

        self.train_generator = train_data_generator.flow_from_directory(directory=self.config.training_data_path, 
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            subset='training',
            shuffle=False
        )

    def train(self, callback_list):
        self.steps_per_epochs = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        history = self.model.fit(self.train_generator, 
                        epochs = self.config.params_epochs,
                        steps_per_epoch = self.steps_per_epochs,
                        validation_steps = self.validation_steps, 
                        validation_data = self.valid_generator,
                        callbacks =callback_list
                        )
        path_to_model_history = os.path.join(os.path.dirname(self.config.trained_model_path), "history_csv")
        create_dirs([path_to_model_history])
        epoch_his_path = os.path.join(
            path_to_model_history,
            f"epoch_his_{self.config.model_no}.csv")
        epoch_history = history.history
        epoch_history_df = pd.DataFrame(epoch_history)
        epoch_history_df.to_csv(epoch_his_path)
        
        trained_model_path = os.path.join(
            os.path.dirname(self.config.trained_model_path),
            f"trained_model_{self.config.model_no}.h5")
        
        self.model.save(trained_model_path)
