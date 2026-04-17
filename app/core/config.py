<<<<<<< HEAD
DATABASE_URL = "sqlite:///./app.db"
SECRET_KEY = "super_secret_key_for_demo_project_change_me"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
REDIS_URL = "redis://localhost:6379/0"
=======
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    DATABASE_URL: str
    REDIS_URL: str

    ENVIRONMENT: str = "development"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
>>>>>>> f288b6a259cfa99c6d34b38d1f98492c44117b3c
