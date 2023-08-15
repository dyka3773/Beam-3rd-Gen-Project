from DataStorage import DataStorage
from Enums.ErrorCodesEnum import ErrorCodesEnum

class CustomException(Exception):    
    
    async def __init__(self, message: str, error: ErrorCodesEnum):
        self.message = message
        self.error = error
        self.error_code = error.value
        
        self.data_manager = await DataStorage()
        
        await self.data_manager.save_error_code(self.error_code)

    def __str__(self):
        return f'{self.message} (Error code: {self.error_code})'