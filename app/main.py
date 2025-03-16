from fastapi import FastAPI
# from app.routers import search
from app.services import open_ai, postgres_data_load, wikipedia, chroma_vector_db

app = FastAPI(title="Load Movie Data (Vector DB)")

# app.include_router(search.router)

@app.get("/")
def home():
    # deepseek_ai.test_deepseek()
    # return deepseek_ai.test_openAI()
    # return open_ai.text_to_embeddings("Cobb, a skilled thief who commits corporate espionage by infiltrating the subconscious of his targets is offered a chance to regain his old life as payment for a task considered to be impossible: \"inception\", the implantation of another person's idea into a target's subconscious.")
    # return {"message": "Welcome to the Movie Search API"}
    # return postgres_data_load.postgres_data_load()
    # return wikipedia.wiki_search()
    # return chroma_vector_db.test_chroma_connection()
    # return postgres_data_load.query_movie_records()
    # return chroma_vector_db.load_embeddings()
    # return chroma_vector_db.query_embeddings("Humans travel to a different planet called pandora in 2154.")
    # return chroma_vector_db.query_embeddings("A hobbit goes on to a fellowship of the ring. The ring is created by dark person. The ring is very powerful, people go to war for the ring.")
    # return chroma_vector_db.query_embeddings("The story is about a hobbit who carries a powerful ring...")
    # return chroma_vector_db.query_embeddings("A hobbit carries a powerful ring...")
    # return chroma_vector_db.query_embeddings("Red Pill and Blue Pill. AI or machines take control over humans...")
    # return chroma_vector_db.query_embeddings("Aliens try to take over earth. US military defeats the aliens and reclaim earth")
    # return chroma_vector_db.query_embeddings("An astroid is about to hit the earth. Astronauts will go on to the astroid and drill down and blast the astroid and save earth from extinction level event...")
    # return chroma_vector_db.query_embeddings("Earth is going extinct, People can't grow food, a lot of sand stroms. A team goes in search of another habitable planet like earth to colonize...")
    # return chroma_vector_db.query_embeddings("A spider bites an man, He is a photographer for a newspaper. Suddenly the man becomes powerful...")
    return chroma_vector_db.query_embeddings("A man wears a suit. The suit is full of technology. The man with the suit is very powerful. He can even fly with the help of the suit...")
    # return chroma_vector_db.collection_details()