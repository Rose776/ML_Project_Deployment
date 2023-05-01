import logging
import os
from datetime import datetime

LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # it is the file name formate of logger
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE_NAME) # it is the file path of the logger file

os.makedirs(logs_path,exist_ok = True) # this os,makedir is used to create directory if directory exist it will no create new thats ehy we use exist_ok = true


LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE_NAME) #it is the entire path of the file including logs directory and file name

print(LOG_FILE_PATH)
logging.basicConfig(

    filename = LOG_FILE_PATH, #file name
    format = "[%(asctime)s] %(lineno)d %(name)s -%(levelname)s - %(message)s", #formateof logging
    level = logging.INFO, #level of logging
)
