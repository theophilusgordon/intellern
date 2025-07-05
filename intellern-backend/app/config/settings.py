from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional
import os

class Settings(BaseSettings):
    # App settings
    app_name: str = "AI Learning Assistant"
    debug: bool = Field(default=False, env="DEBUG")

    # Database settings
    database_url: str = Field(..., env="DATABASE_URL")
    redis_url: str = Field(..., env="REDIS_URL")

    # Auth0 settings
    auth0_domain: str = Field(..., env="AUTH0_DOMAIN")
    auth0_client_id: str = Field(..., env="AUTH0_CLIENT_ID")
    auth0_client_secret: str = Field(..., env="AUTH0_CLIENT_SECRET")
    auth0_audience: str = Field(..., env="AUTH0_AUDIENCE")

    # OpenAI settings
    openai_api_key: str = Field(..., env="OPENAI_API_KEY")

    # Vector store settings
    chroma_persist_directory: str = Field(default="./chroma_db", env="CHROMA_PERSIST_DIR")

    # File upload settings
    max_file_size: int = Field(default=10 * 1024 * 1024, env="MAX_FILE_SIZE")  # 10MB
    upload_directory: str = Field(default="./uploads", env="UPLOAD_DIRECTORY")

    # Speech settings
    whisper_model: str = Field(default="base", env="WHISPER_MODEL")

    # Security settings
    secret_key: str = Field(..., env="SECRET_KEY")
    algorithm: str = Field(default="HS256", env="ALGORITHM")
    access_token_expire_minutes: int = Field(default=30, env="ACCESS_TOKEN_EXPIRE_MINUTES")

    # CORS settings
    allowed_origins: list[str] = Field(default=["http://localhost:4200"], env="ALLOWED_ORIGINS")

    class Config:
        env_file = ".env"
        case_sensitive = False

# Global settings instance
_settings: Optional[Settings] = None

def get_settings() -> Settings:
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings