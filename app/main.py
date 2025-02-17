from fastapi import FastAPI
# from app.routers import search

app = FastAPI(title="Load Movie Data (Vector DB)")

# app.include_router(search.router)

@app.get("/")
def home():
    return {"message": "Welcome to the Movie Search API"}