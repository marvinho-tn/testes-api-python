from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    advice_api_base_url: str
    api_name: str

    class Config:
        env_file = ".env"

settings = Settings()
