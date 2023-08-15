from DataStorage import DataStorage
from Enums.ErrorCodeEnum import ErrorCodeEnum

class CustomException(Exception):    
    
    def __init__(self, message: str, error: ErrorCodeEnum):
        self.message = message
        self.error = error
        self.error_code = error.value
        
        DataStorage().save_error_code(self.error_code)

    def __str__(self):
        return f'{self.message} (Error code: {self.error_code})'