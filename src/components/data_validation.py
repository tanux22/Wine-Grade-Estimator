import os
from src import logger
from src.exception import CustomException
import sys
from src.entity.config_entity import DataValidationConfig
import pandas as pd


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        
    
    def validate_data(self)->bool:
        try:
            validation_status = None
            df=pd.read_csv(self.config.unzip_data_dir)
            logger.info("Data loaded successfully")
            logger.info("Validating data")
            all_columns = list(df.columns)
            all_schema = self.config.all_schema.keys()
            
            for col in all_columns:
                if col not in all_schema:
                    logger.error(f"Column {col} is not in schema")
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write("Data validation failed")
                elif col in all_schema:
                        validation_status = True
                        logger.info(f"Column {col} is in schema")
                        with open(self.config.STATUS_FILE, 'w') as f:
                            f.write("Data validation passed")
            return validation_status
        except Exception as e:
            raise CustomException(e, sys) from e