from pathlib import Path
import joblib
import numpy as np
import pandas as pd
import sys
from src.exception import CustomException
from src import logger
from src.constants import *
from src.utils.common import read_yaml


class PredictionPipeline:
    def __init__(self, config_file_path=CONFIG_FILE_PATH):
        self.config_file_path = config_file_path
    
        self.config = read_yaml(self.config_file_path)
        
    def predict(self, input_data):
        try:
            config = self.config.model_evaluation
            self.model = joblib.load(Path(config.model_path))
            predictions = self.model.predict(input_data)
            logger.info("Predictions made successfully.")
            return predictions
        except Exception as e:
            logger.error(f"Error making predictions: {e}")
            raise CustomException(e, sys)