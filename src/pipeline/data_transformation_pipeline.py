import sys
from src.config.configuration import ConfigurationManager  
from src.components.data_transformation import DataTransformation
from src import logger
from src.exception import CustomException


class DataTransformationPipeline:
    def run(self):
        try:
            logger.info("Data Transformation stage started")
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.train_test_split()
            logger.info("Data Transformation stage completed successfully")
        except Exception as e:
            logger.error(f"Data Transformation failed: {e}")
            raise CustomException(e) from e
