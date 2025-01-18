from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseSignal
import os

class ProjectController(BaseController):

    def __init__(self):
        super().__init__()

    def get_project_path(self,project_id:str):
        project_dir = os.path.join(
            self.files_dir,
            project_id
        )

        if not os.path.exists(project_dir):
            os.makedirs(project_dir)

        return project_dir


    # save uploaded file inside assets
    def save_uploaded_file(self,project_id:str, file:UploadFile):
        file_path = f"assets/files/file_{project_id}"
        with open(file_path,'wb') as f:
            content = file.file.read()
            f.write(content)
        return ResponseSignal.FILE_UPLOAD_SUCCESS.value


