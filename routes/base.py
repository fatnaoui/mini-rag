from fastapi import APIRouter

base_router = APIRouter()

@base_router.get("/")
def welcome():
    return {
        "key":"Hello World!"
    }