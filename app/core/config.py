import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import Field, PostgresDsn, field_validator
from pydantic_core.core_schema import FieldValidationInfo
from typing import Any

# env_file_path: str = os.path.abspath(os.path.dirname("../../.env"))
# load_dotenv(dotenv_path=env_file_path)


class Settings(BaseSettings):
    API_VERSION: str = Field("0.0.1")
    PROJECT_NAME: str = Field("Realty API")
    POSTGRES_ECHO: bool = Field(False)
    POSTGRES_PASSWORD: str = Field("postgres", env="POSTGRES_PASSWORD")
    POSTGRES_USER: str = Field("postgres", env="POSTGRES_USER")
    POSTGRES_HOST: str = Field("localhost", env="POSTGRES_HOST")
    POSTGRES_PORT: str = Field("5432", env="POSTGRES_PORT")
    POSTGRES_DB: str = Field("realty_db", env="POSTGRES_DB")
    POSTGRES_URL: str = Field(env="POSTGRES_URL")


settings = Settings()
