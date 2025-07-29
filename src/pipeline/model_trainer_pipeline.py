from src import logger
from src.exception import CustomException
import sys
from src.entity.config_entity import ModelTrainerConfig
from src.config.configuration import ConfigurationManager
from src.components.model_trainer import ModelTrainer



class ModelTrainerPipeline:
    def run(self):
        try:
            config_manager = ConfigurationManager()
            model_trainer_config = config_manager.get_model_trainer_config()
            model_trainer = ModelTrainer(config=model_trainer_config)
            model_trainer.train()
        except Exception as e:
            logger.error(f"Error occurred during model training: {e}")
            raise CustomException(e, sys) from e
