from CNN_classifier import logger
import os
from pathlib import Path
import json
import yaml
import joblib
from typing import Any
from ensure import ensure_annotations
from box.exceptions import BoxValueError
from box import ConfigBox

@ensure_annotations
def read_yaml(yaml_path_file:Path)->ConfigBox:
    with open(yaml_path_file) as yaml_file:
        content=yaml.safe_load(yaml_file)
        return ConfigBox(content)
    

@ensure_annotations
def save_json():
    pass

@ensure_annotations
def load_json():
    pass

@ensure_annotations
def save_model():
    pass

@ensure_annotations
def load_model():
    pass

def get_size():
    pass

def create_directory(directory_path:list,verbose=True):
    for path in directory_path:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"the repo created at : {path}")
   