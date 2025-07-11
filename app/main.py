from fastapi import  FastAPI
import models


from core import db
from routes import auth_routes,todo_routes


app = FastAPI()
app.include_router(auth_routes.router)
app.include_router(todo_routes.router)

db.Base.metadata.create_all(bind=db.engine)


@app.get("/")
async def index():
    return {"Message": "Welcome to the todo application."}

