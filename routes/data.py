from fastapi import APIRouter, UploadFile, Depends
from helpers.config import get_settings, Settings
from controllers import DataController

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1","data"]
)

@data_router.post("/upload_file/{project_id}")
async def upload_file(project_id: str,file: UploadFile, app_settings: Settings= Depends(get_settings)):

    # validate the file properties
    is_valid, result_signal = DataController().validate_uploaded_file(file=file)
    return is_valid
    