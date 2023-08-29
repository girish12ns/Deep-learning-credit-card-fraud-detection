import os
from box.exceptions import BoxValueError
import yaml
from src.card_fraud_detection import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import dill

@ensure_annotations
def create_directories(filename:list,verbose=True):
    for file in filename:
        os.makedirs(file,exist_ok=True)
        if verbose:
            logger.info("file created")
    
    

@ensure_annotations
def read_yaml(filename)->ConfigBox:

    with open(filename,'r') as f:
        content=yaml.safe_load(f)
    return ConfigBox(content)