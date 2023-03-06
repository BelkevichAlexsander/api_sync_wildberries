from pydantic import BaseSettings, SecretStr
from dotenv import load_dotenv
import os


class Settings(BaseSettings):
    URL_WILDCARD: SecretStr
    DJANGO_SECRET_KEY: SecretStr

    ENGINE: SecretStr
    NAME: SecretStr
    USER: SecretStr
    PASSWORD: SecretStr
    HOST: SecretStr

    class Config:
        dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
        if os.path.exists(dotenv_path):
            load_dotenv(dotenv_path)


# Валидация объекта конфига
config = Settings()
