from enum import Enum

class ResponseSignal(Enum):

    FILE_VALIDATE_SUCCESSFLY = "file validate successfly"
    FILE_TYPE_NOT_SUPPORTED = "file type not supported"
    FILE_SIZE_EXCEEDED = "file size exceeded"
    FILE_UPLOAD_SUCCESS = "file upload success"
    FILE_UPLOAD_FAILED = "file upload failed"