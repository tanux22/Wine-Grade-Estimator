import os
from src import logger
from src.exception import CustomException
import sys
from src.entity.config_entity import DataValidationConfig
from src.config.configuration import ConfigurationManager
from src.components.data_validation import DataValidation



class DataValidationPipeline:
    def run(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_data()
            logger.info("Data validation completed successfully.")
        except Exception as e:
            logger.error(f"Data validation failed: {e}")
            raise CustomException(e) from e