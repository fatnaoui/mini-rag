from fastapi import APIRouter, UploadFile, Depends, status
from fastapi.responses import JSONResponse
from helpers.config import get_settings, Settings
from controllers import DataController, ProjectController
import os

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1","data"]
)

@data_router.post("/upload_file/{project_id}")
async def upload_file(project_id: str,file: UploadFile, app_settings: Settings= Depends(get_settings)):

    # validate the file properties
    is_valid, result_signal = DataController().validate_uploaded_file(file=file)
    
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "result_signal": result_signal
            }
        )
    
    project_dir_path = ProjectController().get_project_path(project_id=project_id)
    project_file_path = os.path.join(
        project_dir_path,
        file.filename
    )
    
    # save the file
    result = ProjectController().save_uploaded_file(file=file,project_id=project_id)
    return result

    