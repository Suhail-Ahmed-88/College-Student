from src.Student_Project.logger import logging
from src.Student_Project.exeception import CustomException
import sys

if __name__ == "__main__":
    logging.info("The Execution has Started")
    
    
    
try:
    a=1/0
except Exception as e:
    logging.info("Custom Exception")
    raise CustomException(e,sys)   