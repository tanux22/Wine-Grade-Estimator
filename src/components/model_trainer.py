import os
from src import logger
from src.exception import CustomException
import sys
import joblib
from sklearn.linear_model import ElasticNet
import pandas as pd
from src.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        try:
            logger.info("Training the model...")
            train_df = pd.read_csv(self.config.train_data_path)
            test_df = pd.read_csv(self.config.test_data_path)
            
            X_train = train_df.drop(columns=[self.config.target_column],axis=1)
            y_train = train_df[self.config.target_column]
            X_test = test_df.drop(columns=[self.config.target_column],axis=1)
            y_test = test_df[self.config.target_column]
            
            lr= ElasticNet(
                alpha=self.config.alpha,
                l1_ratio=self.config.l1_ratio,
                random_state=42
            )
            
            lr.fit(X_train, y_train)
            joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))
            
            logger.info(f"Model trained and saved at {self.config.root_dir / self.config.model_name}")
        except Exception as e:
            raise CustomException(e, sys) from e