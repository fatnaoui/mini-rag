from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME  : str
    APP_VERSION : str
    OPENAI_KEY : str


    class Config():
        env_file = ".env"   # Automaically load the .env file

def get_settings():
    return Settings()