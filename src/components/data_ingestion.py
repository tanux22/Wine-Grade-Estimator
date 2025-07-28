import os
import urllib.request as request
import zipfile
from src.utils.common import get_size
from src import logger
from src.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            logger.info(f"Downloading data from {self.config.source_url} to {self.config.local_data_file}")
            filename, headers=request.urlretrieve(url=self.config.source_url,filename= self.config.local_data_file)
            # logger.info(f"Downloaded {get_size(self.config.local_data_file)} bytes")

    def unzip_data(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            
    
