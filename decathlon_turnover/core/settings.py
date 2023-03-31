# -*- coding: utf-8 -*-

from functools import lru_cache

from pydantic import BaseSettings


# app class settings
class Settings(BaseSettings):
    """Store settings variables and load env variables from .env file."""

    app_version: str = "0.2.0"
    app_name: str = """Decathlon Turnoever Forescasting"""
    app_description: str = """
    In order to help store managers in making mid-term decisions driven
    by economic data, we want to forecast the turnover for the next 8 weeks
    at store-department level in Decathlon."""
    api_prefix: str = ""
    author: str = "Youcef"
    host: str = "0.0.0.0"
    port: str = "5000"

    class Config:
        """Load .env file for env variables."""

        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    """Create and cache settings object.

    Returns
    -------
    Settings
        Settings object
    """
    return Settings()
