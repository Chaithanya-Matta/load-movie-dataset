import pandas as pd
from sqlalchemy import create_engine, text, Column, Integer, String, BigInteger, Text
import ast
from app.core.config import settings
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# PostgreSQL Connection Configurations
DB_USER = settings.POSTGRES_DB_USER
DB_PASSWORD = settings.POSTGRES_DB_PASSWORD
# DB_HOST = "localhost"  # or your cloud DB endpoint
DB_HOST = "host.docker.internal"  # or your cloud DB endpoint
DB_PORT = "5432"
DB_NAME = "mydatabase"

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class MovieNew(Base):
    __tablename__ = "movie_new"

    # id = Column(Integer, primary_key=True, index=True)
    # original_title = Column(String)
    # keywords = Column(String)
    # genres = Column(String)

    id = Column(BigInteger, primary_key=True)
    original_title = Column(Text, nullable=True)
    keywords = Column(Text, nullable=True)
    genres = Column(Text, nullable=True)

def postgres_data_load():

    print("Data load started into PostgreSQL!")

    # Read CSV File
    csv_file = "/Users/chaithanyamanasreddymatta/Downloads/TMDB_movie_dataset_v11.csv"  # Replace with your actual file path 
    df = pd.read_csv(csv_file)

    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    df['adult'] = df['adult'].astype(bool)
    df['vote_average'] = df['vote_average'].astype(float)
    df['vote_count'] = df['vote_count'].astype(int)
    df['revenue'] = df['revenue'].astype(int)
    df['budget'] = df['budget'].astype(int)
    df['runtime'] = df['runtime'].astype(int)
    df['popularity'] = df['popularity'].astype(float)

    df['genres'] = df['genres'].apply(convert_to_list)
    df['production_companies'] = df['production_companies'].apply(convert_to_list)
    df['production_countries'] = df['production_countries'].apply(convert_to_list)
    df['spoken_languages'] = df['spoken_languages'].apply(convert_to_list)
    df['keywords'] = df['keywords'].apply(convert_to_list)


    # Insert Data into PostgreSQL
    df.to_sql("movie", engine, if_exists="append", index=False)

    print("Data successfully inserted into PostgreSQL!")

    return "Success"

# Convert string-based lists into actual Python lists
def convert_to_list(value):
    if isinstance(value, str):
        return value.split(", ")  # Split by ", " to form a list
    return []

def query_movie_records():

    query = "select id, original_title, keywords, genres from public.movie_new limit 10;"

    with engine.connect() as conn:
        result = conn.execute(text(query))

        movies = [
                {"id": row[0], "original_title": row[1], "keywords": row[2], "genres": row[3]}
                for row in result
            ]

        for row in movies:

            print(row)

    return movies