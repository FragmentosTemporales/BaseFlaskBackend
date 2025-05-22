import os
from datetime import timedelta
from .settings import settings as s


basedir = os.path.abspath(os.path.dirname(__file__))


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
    SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:5432/dbDesafio"
    pool_reset_on_return = None


class TestConfig(BaseConfig):
    """ Testing configuration class """
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
        basedir, "..", 'dbTest.db'
    )
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    "dev": DevConfig,
    "test": TestConfig
    }
