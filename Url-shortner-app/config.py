# shortener_app/config.py
from functools import lru_cache
from sys import BaseSettings

class Settings(BaseSettings):
    env_name: str = "Local"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite:///./shorturl.db"

@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"The settings are loaded for: {settings.env_name}")
    return settings

class Config:
        env_file = ".env"
