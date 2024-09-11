from src.Student_Project.logger import logging
from src.Student_Project.exeception import CustomException
from src.Student_Project.components.data_ingestion import DataIngestion
from src.Student_Project.components.data_ingestion import DataIngestionConfig 
import sys
import os
import pymysql

if __name__ == "__main__":
    logging.info("The Execution has Started")
    
    
    
try:
    # deta_ingestion_config=DataIngestionConfig()
    data_ingestion=DataIngestion()
    data_ingestion.initiate_data_ingestion()
except Exception as e:
    logging.info("Custom Exception")
    raise CustomException(e,sys)   