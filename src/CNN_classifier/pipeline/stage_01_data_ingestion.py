from CNN_classifier.components.stage_01_data_ingestion import DataIngestion
import os 
from CNN_classifier.config import ConfigurationManager
from CNN_classifier import logger

config=ConfigurationManager()
data_ingestion_config=config.get_data_ingestion_config()

data_ingestion=DataIngestion()