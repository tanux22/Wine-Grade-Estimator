from src.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH
from src.utils.common import read_yaml, create_directories
from pathlib import Path
from src.entity.config_entity import DataIngestionConfig
from src.entity.config_entity import DataValidationConfig
from src.entity.config_entity import DataTransformationConfig
from src.entity.config_entity import ModelTrainerConfig
from src.entity.config_entity import ModelEvaluationConfig


class ConfigurationManager:
    def __init__(self, config_file_path=CONFIG_FILE_PATH, params_file_path=PARAMS_FILE_PATH, schema_file_path=SCHEMA_FILE_PATH):

        self.config_file_path = config_file_path
        self.params_file_path = params_file_path
        self.schema_file_path = schema_file_path

        self.config = read_yaml(self.config_file_path)
        self.params = read_yaml(self.params_file_path)
        self.schema = read_yaml(self.schema_file_path)

        create_directories([self.config.artifacts_root])

        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir, config.unzip_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_url=config.source_url,
            local_data_file=Path(config.local_data_file),
            unzip_dir=Path(config.unzip_dir)
        )
        
        return data_ingestion_config
    
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS.to_dict()
        create_directories([config.root_dir])
        
        data_validation_config = DataValidationConfig(
            root_dir=Path(config.root_dir),
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir=Path(config.unzip_data_dir),
            all_schema=schema
        )
        
        return data_validation_config
    
    
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        
        create_directories([config.root_dir])
        
        data_transformation_config = DataTransformationConfig(
            root_dir=Path(config.root_dir),
            data_path=Path(config.data_path)
        )
        
        return data_transformation_config
    
    
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN
        
        create_directories([Path(config.root_dir)])
        
        model_trainer_config = ModelTrainerConfig(
            root_dir=Path(config.root_dir),
            train_data_path=Path(config.train_data_path),
            test_data_path=Path(config.test_data_path),
            model_name=config.model_name,
            alpha=params.alpha,
            l1_ratio=params.l1_ratio,
            target_column=schema.name
        )
        
        return model_trainer_config
    
    
    
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        """
        Returns the configuration for model evaluation.
        """
        config = self.config.model_evaluation
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN
        
        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=Path(config.root_dir),
            test_data_file_path=Path(config.test_data_file_path),
            model_path=Path(config.model_path),
            all_params=dict(params),
            evaluation_report=Path(config.evaluation_report),
            target_column=schema.name,
            mlflow_uri="https://dagshub.com/atanushreddy/Wine-Grade-Estimator.mlflow"
        )

        return model_evaluation_config
    
    
    
    