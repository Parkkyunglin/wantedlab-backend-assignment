from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    MYSQL_HOST: str
    MYSQL_PORT: str
    MYSQL_PASSWORD: str
    MYSQL_DATABASE: str
    MYSQL_USER: str

    class Config:
        env_file = ".env"


@lru_cache()
def get_setting():
    return Settings()


supported_languages = ["ko", "en", "ja", "tw"]
fallback_language = "ko"
