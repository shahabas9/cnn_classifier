from CNN_classifier.components.stage_01_data_ingestion import DataIngestion
import os 
from CNN_classifier.config.configuaration import ConfigurationManager
from CNN_classifier import logger

logger.info(f"data ingestion stage starting")

config=ConfigurationManager()
data_ingestion_config=config.get_data_ingestion_config()

data_ingestion=DataIngestion(config=data_ingestion_config)
data_ingestion.download_data()
data_ingestion.unzip_and_clean()

logger.info(f"data ingestion stage completed sucessfully")