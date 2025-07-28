import os
from pathlib import Path
from src import logger
from box import ConfigBox
import json
from typing import List
import yaml
import joblib
from ensure import ensure_annotations
from typing import Any, Dict, List, Union
from src.exception import CustomException
import sys

@ensure_annotations
def read_yaml(file_path: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as ConfigBox.
    
    Args:
        file_path (str): Path to the YAML file.
        
    Returns:
        ConfigBox: Content of the YAML file.
    """
    try:
        with open(file_path, 'r') as file:
            content = yaml.safe_load(file)
            logger.info(f"YAML file {file_path} read successfully.")
            return ConfigBox(content)
    except Exception as e:
        raise CustomException(e, sys) from e
    
    
    

def create_directories(path_to_dirs: List[Path], verbose: bool = True) -> None:
    """
    Creates directories if they do not exist.
    
    Args:
        dirs (List[str]): List of directory paths to create.
    """
    for dir_path in path_to_dirs:
        os.makedirs(dir_path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created: {dir_path}")       
            
    
    
@ensure_annotations
def save_json(file_path: Path, data: dict) -> None:
    """
    Saves data to a JSON file.
    
    Args:
        file_path (Path): Path to the JSON file.
        data (Union[Dict, List]): Data to save.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            logger.info(f"Data saved to JSON file: {file_path}")
    except Exception as e:
        raise CustomException(e, sys) from e
    
    
    
    
@ensure_annotations
def load_json(file_path: Path) -> ConfigBox:
    """
    Loads data from a JSON file.
    
    Args:
        file_path (Path): Path to the JSON file.
        
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            logger.info(f"Data loaded from JSON file: {file_path}")
            return ConfigBox(data)
    except Exception as e:
        raise CustomException(e, sys) from e
    
    
    
    
    
@ensure_annotations
def load_bins(file_path: Path) -> Any:
    """
    Loads bin edges from a JSON file.
    
    Args:
        file_path (Path): Path to the JSON file containing bin edges.
        
    Returns:
        Any
    """
    try:
        with open(file_path, 'r') as file:
            bins = json.load(file)
            logger.info(f"Bins loaded from JSON file: {file_path}")
            return bins
    except Exception as e:
        raise CustomException(e, sys) from e
        
        
        

@ensure_annotations
def get_size(file_path: Path) -> str:
    """
    Returns the size of a file in bytes.
    
    Args:
        file_path (Path): Path to the file.
        
    Returns:
        str: Size of the file in bytes.
    """
    try:
        size = os.path.getsize(file_path)
        logger.info(f"Size of file {file_path}: {size} bytes")
        return size
    except Exception as e:
        raise CustomException(e, sys) from e