import sys

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    
    error_message = "Error occure in python script name [{0}] Line number [{1}] Error message [{2}]".format(file_name,line_number,(str(error))
    )
    return error_message

class CustomException(Exception): #Creating a Custom exception we are inheriting SUPER class called Exception
    def __init__(self,error_message,error_detail:sys):
        """ we are passing the Error Exception as e to the SUPER class which can we (zero division error) and we pass (sys) which is a python module 
        which contains the data of how the program run what user typed and many more we use thi sys module to get the data where the error occure, error linke number and file name etc"""
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
        print(sys)

    def __str__(self): # function use to formate the message in a cutome formate
        return self.error_message

