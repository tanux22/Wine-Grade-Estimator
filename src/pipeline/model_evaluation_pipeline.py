from src import logger
from src.exception import CustomException
import sys
from src.entity.config_entity import ModelEvaluationConfig
from src.config.configuration import ConfigurationManager
from src.components.model_evaluation import ModelEvaluation



class ModelEvaluationPipeline:
    """    This class is responsible for evaluating the model's performance using metrics like MSE and R2 score
    and logging the results into MLflow.
    """
    def run(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(config=model_evaluation_config)
            model_evaluation.log_into_mlflow()
            logger.info("Model evaluation completed successfully.")
        except Exception as e:
            logger.error(f"Model evaluation failed: {e}")
            raise CustomException(e,sys) from e