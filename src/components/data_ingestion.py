import os
import sys
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split

from dataclasses import dataclass
from src.components.data_transformation import DataTransformation,  DataTransformationConfig



@dataclass
class DataIngestionConfig:
    raw_data_path:str = os.path.join("artifacts", "data.csv")
    train_data_path:str = os.path.join("artifacts", "train.csv")
    test_data_path:str = os.path.join("artifacts", "test.csv")

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Entered into Data Ingestion Component")
        try:
            data = pd.read_csv("notebook\data\stud.csv")
            logging.info("Read Dataset as dataframe")

            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path),exist_ok=True)
            
            data.to_csv(self.data_ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Raw data saved")
            train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
            logging.info("Train data saved")
            train_data.to_csv(self.data_ingestion_config.train_data_path,index=False,header=True)
            logging.info("Test Data saved")
            test_data.to_csv(self.data_ingestion_config.test_data_path,index=False,header=True)

            return(self.data_ingestion_config.train_data_path, self.data_ingestion_config.test_data_path)


        except Exception as e:
            raise CustomException(e,sys)
        

if __name__ == "__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)