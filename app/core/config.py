from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

class Settings(BaseSettings):
    WEAVIATE_DB_URL: str = os.getenv("WEAVIATE_DB_URL")
    WEAVIATE_API_KEY: str = os.getenv("WEAVIATE_API_KEY")
    DEEPSEEK_URL: str = os.getenv("DEEPSEEK_URL")
    DEEPSEEK_API_KEY: str = os.getenv("DEEPSEEK_API_KEY")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")

    class Config:
        env_file = ".env"  # Optional: Automatically loads from .env

settings = Settings()
