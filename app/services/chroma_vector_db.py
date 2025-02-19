# from app.core.config import settings
import chromadb
from chromadb.config import Settings

settings = Settings(chroma_server_host="localhost", chroma_server_http_port=8001)
client = chromadb.Client(settings=settings)

def test_chroma_connection():

    # List existing collections (should return an empty list if none exist)
    collections = client.list_collections()
    print("Available collections:", collections)

    # Create a test collection
    collection = client.create_collection(name="test_collection")
    print("Collection created:", collection.name)

    # List collections again to confirm
    collections = client.list_collections()
    print("Updated collections:", collections)

    return ""


# # Create a collection
# collection = client.create_collection(name="movies")

# # Add some data
# collection.add(
#     ids=["1"],
#     documents=["The Matrix is a sci-fi movie about a dystopian future."],
#     metadatas=[{"genre": "sci-fi"}]
# )

# # Query the data
# results = collection.query(
#     query_texts=["dystopian sci-fi"],
#     n_results=1
# )

# print(results)



