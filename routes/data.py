from fastapi import APIRouter, UploadFile, Depends
from helpers.config import get_settings, Settings

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1","data"]
)

@data_router.post("/upload/{project_id}")
async def upload_file(project_id: str,file = UploadFile, app_settings: Settings= Depends(get_settings)):
    pass
    