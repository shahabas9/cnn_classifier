import os
import urllib.request as request
from zipfile import ZipFile
from CNN_classifier import logger
from tqdm import tqdm
from pathlib import Path
from CNN_classifier.entity import DataIngestionConfig
from CNN_classifier.utils import utils


 class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
    def get_updated_list_of_files(self,list_of_files):
        return [f for f in list_of_files if f.endswith(".jpg")]
    
    def preprocess(self, zf: ZipFile, f: str, working_dir: str):
        target_filepath = os.path.join(working_dir, f)
        if not os.path.exists(target_filepath):
            zf.extract(f, working_dir)
            
    def unzip_and_clean(self):
        with ZipFile(file=self.config.local_data_file, mode="r") as zf:
            list_of_files = zf.namelist()
            updated_list_of_files = self.get_updated_list_of_files(list_of_files)
            for f in updated_list_of_files:
                self.preprocess(zf, f, self.config.unzip_dir)
