from fastapi import  FastAPI
import models


from core import db


app = FastAPI()

db.Base.metadata.create_all(bind=db.engine)


@app.get("/")
async def index():
    return {"Message": "Hello Woerld"}

