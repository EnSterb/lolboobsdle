from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DB_USERNAME = getenv("POSTGRES_USER")
DB_PASSWORD = getenv("POSTGRES_PASSWORD")
DB_PORT = getenv("POSTGRES_PORT")
DB_NAME = getenv("POSTGRES_DB")
DB_HOST = getenv("POSTGRES_HOST")

engine = create_engine(f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        # print("Database session started")
        yield db
    except Exception as e:
        db.rollback()
        print(f"Error occurred: {e}")
    finally:
        db.close()