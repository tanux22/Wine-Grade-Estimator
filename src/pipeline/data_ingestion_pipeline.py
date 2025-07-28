from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion
from src import logger   
from src.exception import CustomException
import sys

STAGE_NAME = "Data Ingestion stage"

class DataIngestionPipeline:
    def __init__(self):
        self.config_manager = ConfigurationManager()
        self.data_ingestion_config = self.config_manager.get_data_ingestion_config()
        self.data_ingestion = DataIngestion(config=self.data_ingestion_config)

    def run(self):
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
        self.data_ingestion.download_data()
        self.data_ingestion.unzip_data()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<")
        
if __name__ == "__main__":
    try:
        data_ingestion_pipeline = DataIngestionPipeline()
        data_ingestion_pipeline.run()
    except Exception as e:
        logger.exception(e)
        raise CustomException(e, sys) from e    
    finally:
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} finished <<<<<<<<<<<")
        logger.info(f"Pipeline execution completed.")