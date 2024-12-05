import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pathlib import Path

load_dotenv()


class FastAPIPYTestBase(BaseSettings):
    PROJECT_NAME: str = "FastAPI PYTesBase"
    BASE_DIR: str = str(Path().absolute())


class FastAPIPYTestDB(FastAPIPYTestBase):
    DB_NAME: str = os.environ.get("DB_NAME")
    DB_HOST: str = os.environ.get("DB_HOST")
    DB_PORT: int = os.environ.get("DB_PORT")
    DB_USER: str = os.environ.get("DB_USER")
    DB_PASSWORD: str = os.environ.get("DB_PASSWORD")

    @property
    def get_db_uri(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:" \
               f"{self.DB_PORT}/{self.DB_NAME}"


class FastAPIPYTestSettings(FastAPIPYTestDB):
    DEBUG: bool
    postgres: FastAPIPYTestDB = FastAPIPYTestDB()


def get_settings(db_only=False):
    if not db_only:
        return FastAPIPYTestSettings()
    else:
        return FastAPIPYTestDB()

