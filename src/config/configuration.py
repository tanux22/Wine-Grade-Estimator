from src.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH
from src.utils.common import read_yaml, create_directories
from pathlib import Path
from src.entity.config_entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(self, config_file_path=CONFIG_FILE_PATH, params_file_path=PARAMS_FILE_PATH, schema_file_path=SCHEMA_FILE_PATH):
        # ✅ Save parameters as instance variables
        self.config_file_path = config_file_path
        self.params_file_path = params_file_path
        self.schema_file_path = schema_file_path

        # ✅ Now you can use them
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
    
    
    