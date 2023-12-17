import os
import urllib.request as request
from zipfile import ZipFile
from CNN_classifier import logger
from tqdm import tqdm
from pathlib import Path
from CNN_classifier.entity import DataIngestionConfig
from CNN_classifier.utils import utils


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
    
    def download_data(self):
        pass
    
    def get_updated_list_of_files(self):
        pass
    
    def preprocess(self):
        pass

    def unzip_and_clean(self):
        pass
