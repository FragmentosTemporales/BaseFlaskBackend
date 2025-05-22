from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):

    flask_env: str
    jwt_secret_key: str
    jwt_access_token_expires_hours: int
    jwt_access_token_expires_days: int
    secret_key: str

    dbuser : str
    dbpassword : str

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), '..', '.env')


settings = Settings()
