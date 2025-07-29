import os
from src import logger
from src.exception import CustomException
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from src.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        
       
    def train_test_split(self):
        try:
            df = pd.read_csv(self.config.data_path)
            train,test=train_test_split(df, test_size=0.2, random_state=42)
            train.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index=False)
            test.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index=False)
            logger.info("Data split into train and test sets successfully.")
            logger.info(train.shape)
            logger.info(test.shape)
        except Exception as e:
            raise CustomException(e,sys) from e   
    