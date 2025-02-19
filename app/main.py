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
    return chroma_vector_db.test_chroma_connection()