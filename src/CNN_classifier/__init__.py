import os
import sys
import logging
import time

log_dir="logs"
log_path=os.path.join(log_dir,f"log_{time.time()}.log")
os.makedirs(log_dir,exist_ok=True)
logging_str="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_path),
        logging.StreamHandler(sys.stdout)
    ]
)
logger=logging.getLogger("cnn_classifier")