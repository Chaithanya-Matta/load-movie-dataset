import chromadb
from chromadb.config import Settings
from app.core.config import settings
from datetime import datetime   
import chromadb.utils.embedding_functions as embedding_functions
from app.services.open_ai import text_to_embeddings
from app.services import postgres_data_load, wikipedia 

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

    movie_collection_name = "movie_collection"

    print(client.heartbeat())

    client.delete_collection(collection_name)

    collections = client.list_collections()
    print("Collections:", collections)
 
    # collection = client.get_collection("test_collection")

    collection = client.create_collection(
        name=movie_collection_name,
        metadata={
            "description": "Movie collection holds all the movie related embeddings",
            "created": str(datetime.now())
        } 
    )
    document_text = "The Matrix is a sci-fi movie about a dystopian future."
    embedding = text_to_embeddings(document_text)

    print("Embeddings: ", embedding)

    # Add some data
    # collection.add(
    #     ids=["1"],
    #     # documents=[document_text],
    #     embeddings=[embedding],
    #     # metadatas=[{"genre": "sci-fi"}]
    # )    

    # data = collection.get(
    #     ids=["1"],
    #     include=["embeddings"]
    # )

    # print("Queried Data: ", data)




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


def load_embeddings():
    collection_name = "movie_collection"

    # client.delete_collection(collection_name)

    # collection = client.create_collection(
    #     name=collection_name,
    #     metadata={
    #         "description": "Movie collection holds all the movie related embeddings",
    #         "created": str(datetime.now())
    #     } 
    # )

    collection = client.get_collection(collection_name)

    movies = postgres_data_load.query_movie_records()
    print("*********************************************START VECTOR LOAD**************************************************************")

    for row in movies:

    #     # print(row.get("keywords"))
        print("*********************************************START**************************************************************")
        id = str(row.get('id'))
        print(row.get("original_title"))
        print(row.get("release_year"))
        wikiData = wikipedia.wiki_search(row.get('original_title'), row.get('release_year'))
        print(wikiData)
        embedding = text_to_embeddings(wikiData)

        collection.add(
            ids=[id],
            embeddings=[embedding],
        )   
        postgres_data_load.update_plot('updated', id)


        print("**********************************************END***************************************************************")


    # print(wikipedia.wiki_search('Pulp Fiction', '1994'))

    # postgres_data_load.update_plot("Test plot", '27205')
    print("*********************************************END VECTOR LOAD**************************************************************")


    return ""


def query_embeddings(query:str):
    collection_name = "movie_collection"
    collection = client.get_collection(collection_name)

    embedding = text_to_embeddings(query)

    result = collection.query(
        query_embeddings=embedding,
        n_results=10
    )

    ids = ", ".join(result.get('ids')[0])

    response = postgres_data_load.query_movie_title(ids)

    return response

def collection_details():
    collection_name = "movie_collection"

    collection = client.get_collection(collection_name)

    count = collection.count()
    return count