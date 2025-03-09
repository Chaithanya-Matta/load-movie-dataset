import chromadb
from chromadb.config import Settings
from app.core.config import settings
from datetime import datetime   
import chromadb.utils.embedding_functions as embedding_functions
from app.services.open_ai import text_to_embeddings

client = chromadb.HttpClient(
    # host="chromadb",
    host="host.docker.internal", 
    port=8000,
    settings=Settings(
        allow_reset=True,
        anonymized_telemetry=False
    )
)

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=settings.OPENAI_API_KEY,
    model_name="text-embedding-3-small"
)

def test_chroma_connection():

    collection_name = "test_collection"

    print(client.heartbeat())

    client.delete_collection(collection_name)

    collections = client.list_collections()
    print("Collections:", collections)
 
    # collection = client.get_collection("test_collection")

    collection = client.create_collection(
        name=collection_name,
        # embedding_function=openai_ef,
        metadata={
            "description": "my first Chroma collection",
            "created": str(datetime.now())
        } 
    )
    document_text = "The Matrix is a sci-fi movie about a dystopian future."
    embedding = text_to_embeddings(document_text)

    print("Embeddings: ", embedding)

    # Add some data
    collection.add(
        ids=["1"],
        documents=[document_text],
        embeddings=[embedding],
        metadatas=[{"genre": "sci-fi"}]
    )    

    data = collection.get(
        ids=["1"],
        include=["embeddings"]
    )

    print("Queried Data: ", data)




    # print("Collection created:", collection.configuration_json)

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



