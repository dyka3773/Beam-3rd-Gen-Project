import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
# The above code is a hack used to import modules from the parent directory. 
# NOTE: I DO NOT recommend using this in production code.

from DataStorage import DataStorage
from ErrorHandling.ErrorCode import ErrorCode

class CustomException(Exception):    
    
    def __init__(self, message: str, error: ErrorCode):
        self.message = message
        self.error = error
        self.error_code = error.value
        
        DataStorage().save_error_code(self.error_code)

    def __str__(self):
        return f'{self.message} (Error code: {self.error_code})'