from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APPLICATION_VERSION: str = "dev"
    TEST_MODE: bool = False
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/travel_db"

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    return Settings()