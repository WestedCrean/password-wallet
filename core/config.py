import os

from pydantic import BaseSettings


class Config(BaseSettings):
    ENV: str = "development"
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    DB_URL: str = "sqlite:///testdb.sqlite"
    JWT_SECRET_KEY: str = "fastapi"
    JWT_ALGORITHM: str = "HS256"


class DevelopmentConfig(Config):
    DB_URL: str = "sqlite:///testdb.sqlite"


class LocalConfig(Config):
    DB_URL: str = "sqlite:///testdb.sqlite"


class ProductionConfig(Config):
    DEBUG: str = False
    DB_URL: str = "sqlite:///testdb.sqlite"


def get_config():
    env = os.getenv("ENV", "local")
    config_type = {
        "development": DevelopmentConfig(),
        "local": LocalConfig(),
        "production": ProductionConfig(),
    }
    return config_type[env]


config: Config = get_config()
