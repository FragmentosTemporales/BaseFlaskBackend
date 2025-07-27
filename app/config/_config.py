import os
from datetime import timedelta
from pydantic_settings import BaseSettings


basedir = os.path.abspath(os.path.dirname(__file__))


class Settings(BaseSettings):

    jwt_secret_key: str
    jwt_access_token_expires_hours: int
    jwt_access_token_expires_days: int
    secret_key: str

    dbuser: str
    dbpassword: str
    dbhost: str
    dbschema: str

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), '..', '..', '.env')


s = Settings()


class BaseConfig:
    """ Base configuration application class """
    JWT_SECRET_KEY = s.jwt_secret_key
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(
        hours=int(s.jwt_access_token_expires_hours)
    )
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(
        days=int(s.jwt_access_token_expires_days)
    )
    SECRET_KEY = s.secret_key


class DevConfig(BaseConfig):
    """ Development configuration class """
    POSTGRES_USER = s.dbuser
    POSTGRES_PASSWORD = s.dbpassword
    POSTGRES_HOST = s.dbhost
    POSTGRES_SCHEMA = s.dbschema
    SQLALCHEMY_DATABASE_URI = (
        f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@'
        f'{POSTGRES_HOST}/{POSTGRES_SCHEMA}'
    )
    pool_reset_on_return = None


class TestConfig(BaseConfig):
    """ Testing configuration class """
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
        basedir, "..", "..", 'dbTest.db'
    )
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    "dev": DevConfig,
    "test": TestConfig
    }
