from fastapi import FastAPI
from sqlalchemy import text
from app import models
from app.database import Base, engine

app = FastAPI()

# database table creations
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Cricket stat api is working."}


@app.get("/test-db")
def test_database():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            return {"database": "connect", "result": result.scalar()}
    except Exception as e:
        return {"database": "connection failed", "error": str(e)}
