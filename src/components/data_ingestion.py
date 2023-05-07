import os
import sys
sys.path.append('../')
from src.logger import logging
from src.exception import CustomException
from src.utils import read_data
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass 
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts','train.csv')
    test_data_path: str = os.path.join('artifacts','test.csv')
    raw_data_path: str = os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_paths = DataIngestionConfig()

    
    def initiate_DataIngestion(self):

        try:
            data = read_data("notebook/Data.csv")
            df = data.data_reading_initiated()
            
            os.makedirs(os.path.dirname('artifacts/'),exist_ok=True)
            df.to_csv(self.ingestion_paths.raw_data_path,index=False,header =True)
            train_set , test_set = train_test_split(df,test_size = 0.2,random_state = 32)

            train_set.to_csv(self.ingestion_paths.train_data_path,index = False,header =True)
            test_set.to_csv(self.ingestion_paths.test_data_path,index = False,header =True)
            print(self.ingestion_paths.train_data_path)
            return (
                self.ingestion_paths.train_data_path,
                self.ingestion_paths.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)


if __name__ == "__main__":
    obj =DataIngestion()
    obj.initiate_DataIngestion()