from src import logger
from src.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.exception import CustomException
import sys
from src.pipeline.data_validation_pipeline import DataValidationPipeline
from src.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline


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



STAGE_NAME = "Data Validation stage"
try:
    data_validation_pipeline = DataValidationPipeline()
    data_validation_pipeline.run()
except Exception as e:
    logger.exception(e)
    raise CustomException(e, sys) from e    
finally:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} finished <<<<<<<<<<<")
    logger.info(f"Pipeline execution completed.")
    
logger.info("Application started")



STAGE_NAME = "Data Transformation stage"
try:
    data_transformation_pipeline = DataTransformationPipeline()
    data_transformation_pipeline.run()
except Exception as e:
    logger.exception(e)
    raise CustomException(e, sys) from e    
finally:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} finished <<<<<<<<<<<")
    logger.info(f"Pipeline execution completed.")
    
logger.info("Application started")




STAGE_NAME = "Model Training stage"
try:
    model_training_pipeline = ModelTrainerPipeline()
    model_training_pipeline.run()
except Exception as e:
    logger.exception(e)
    raise CustomException(e, sys) from e    
finally:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} finished <<<<<<<<<<<")
    logger.info(f"Pipeline execution completed.")
    
logger.info("Application started")




STAGE_NAME = "Model Evaluation stage"
try:
    model_evaluation_pipeline = ModelEvaluationPipeline()
    model_evaluation_pipeline.run()
except Exception as e:
    logger.exception(e)
    raise CustomException(e, sys) from e    
finally:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} finished <<<<<<<<<<<")
    logger.info(f"Pipeline execution completed.")
    
logger.info("Application started")