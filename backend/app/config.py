import os
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    APP_NAME: str = "GSK MEDIAVERSE API"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    PORT: int = int(os.getenv("PORT", 8000))
    HOST: str = os.getenv("HOST", "0.0.0.0")
    
    # CORS
    ALLOWED_ORIGINS: List[str] = ["*"]
    
    # Storage
    TEMP_DIR: str = os.getenv("STORAGE_TEMP_DIR", os.path.join(os.path.dirname(__file__), "..", "temp_storage"))
    MAX_UPLOAD_SIZE_MB: int = int(os.getenv("MAX_UPLOAD_SIZE_MB", 100))
    CLEANUP_INTERVAL_MINUTES: int = int(os.getenv("CLEANUP_INTERVAL_MINUTES", 15))
    FILE_TTL_SECONDS: int = 1800  # 30 minutes
    
    # Rate Limiting
    RATE_LIMIT_PER_MINUTE: int = int(os.getenv("RATE_LIMIT_PER_MINUTE", 60))

    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()

# Ensure temp directory exists
os.makedirs(settings.TEMP_DIR, exist_ok=True)
