from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    advice_api_base_url: str
    app_name: str
    rabbitmq_host: str
    mongo_host: str
    mongo_port: int

    class Config:
        env_file = ".env"

settings = Settings()
