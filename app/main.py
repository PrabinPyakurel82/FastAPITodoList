from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from sqlalchemy import text

from core import db


app = FastAPI()

db.Base.metadata.create_all(bind=db.engine)


@app.get("/")
async def index():
    return {"Message": "Hello Woerld"}


@app.get("/test-db")
def test_db_connection(database: Session = Depends(db.get_db)):
    try:
        database.execute(text("SELECT 1"))
        return {"message": "Database connection is working!"}
    except Exception as e:
        return {"message": f"Database connection failed: {e}"}