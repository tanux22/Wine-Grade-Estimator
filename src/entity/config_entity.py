from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path
    
    
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path 
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict
    

@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    
    

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path 
    train_data_path: Path 
    test_data_path: Path
    model_name: str
    alpha: float 
    l1_ratio: float
    target_column: str
    
    

@dataclass(frozen=True)
class ModelEvaluationConfig:
    """
    Configuration for model evaluation.
    """
    root_dir: Path 
    test_data_file_path: Path
    model_path :Path
    all_params : dict
    evaluation_report : Path
    target_column: str
    mlflow_uri: str