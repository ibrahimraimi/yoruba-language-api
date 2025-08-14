from pydantic_settings import BaseSettings
from typing import Optional, List


class Settings(BaseSettings):
    # Database settings
    database_url: str = "sqlite:///./yoruba.db"
    
    # API settings
    api_key: Optional[str] = None
    debug: bool = True
    
    # CORS settings
    cors_origins: List[str] = ["*"]
    
    # OpenAI settings (for future AI features)
    openai_api_key: Optional[str] = None
    ai_model: str = "gpt-4o"
    
    # Server settings
    host: str = "0.0.0.0"
    port: int = 8000
    
    # Rate limiting (for future implementation)
    rate_limit_per_minute: int = 60
    
    class Config:
        env_file = ".env"
        case_sensitive = False
        extra = "ignore"  # Ignore extra fields instead of raising errors


settings = Settings()
