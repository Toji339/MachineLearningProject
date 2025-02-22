import sys
from src.logger import logging
"""
the sys module in py provides access to system - specific parameters and
functions, allowing interaction with the python interpreter and the operating
system.
"""

def error_message_details(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() # two _, _ because first two things are not important
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error Occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    
    return error_message
    
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail=error_detail)
        
    def __str__(self):
        return self.error_message
    

        