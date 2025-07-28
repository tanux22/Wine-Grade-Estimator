from src import logger
from src.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.exception import CustomException
import sys


STAGE_NAME = "Data Ingestion stage"
try:
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.run()
except Exception as e:
    logger.exception(e)
    raise CustomException(e, sys) from e    
finally:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} finished <<<<<<<<<<<")
    logger.info(f"Pipeline execution completed.")


logger.info("Application started")