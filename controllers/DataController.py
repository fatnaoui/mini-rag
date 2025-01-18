from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseSignal

class DataController(BaseController):
    
    def __init__(self):
        super().__init__()
        self.size_scale = 1048576 # tp convert MB tp Byte, cuz file.size gives the size in Bytes

    # Validate Function File
    def validate_uploaded_file(self,file: UploadFile):

        if (file.size > self.app_settings.FILE_ALLOWED_SIZE*self.size_scale):
            return False, ResponseSignal.FILE_SIZE_EXCEEDED.value
        
        if (file.content_type not in self.app_settings.FILE_ALLOWED_TYPES):
            return False, ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value
            
        return True, ResponseSignal.FILE_UPLOAD_SUCCESS.value
        
