from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    llm_provider: str = "localai"
    llm_api_key: Optional[str] = None
    # For LocalAI, this doesn't matter since LocalAI controls the model separately,
    # but kept for compatibility with other providers
    llm_model: str = "phi"
    llm_base_url: str = "http://localhost:11434/v1"

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()
