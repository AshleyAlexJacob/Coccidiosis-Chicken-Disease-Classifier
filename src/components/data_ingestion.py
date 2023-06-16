import os
import urllib.request as request
import zipfile
from src.logging import logger
from src.utils.commons import get_size
from src.entity.config_entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            file_name, headers = request.urlretrieve(
                url  = self.config.source_url,
                filename= self.config.local_data_file,
            )
            logger.info(f"{file_name} Downloaded Successfully ✅ with following info {headers}")
        
        else:
            print('IM in else')
            logger.info(f"File already exists with same size: {get_size(Path(self.config.local_data_file))}")
    
    def extract_zip_file(self):
        """
        zip_file_path:str
        Extracts the zip file into the data directory
        Return: Nothing
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok= True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        os.remove(self.config.local_data_file)