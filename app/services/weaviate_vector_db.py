import weaviate
from app.core.config import settings

# Set up Weaviate connection
client = weaviate.Client(
    url=settings.WEAVIATE_DB_URL,
    auth_client_secret=weaviate.AuthApiKey(api_key=settings.WEAVIATE_API_KEY),
)



