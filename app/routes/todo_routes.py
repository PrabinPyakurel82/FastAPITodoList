from typing import List

from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session

from core.db import get_db
from core.deps import get_current_user
from models import User, Todo
from schemas import TodoCreate, TodoUpdate, TodoOut
import crud

router = APIRouter(prefix='/todos', tags=["Tosos"])


@router.get("/",response_model=List[TodoOut])
def get_todos(db:Session = Depends(get_db), current_user:User =  Depends(get_current_user)):
    return crud.get_user_todos(db,user_id=current_user.id)


@router.post("/",response_model=TodoOut, status_code=status.HTTP_201_CREATED)
def todo_create(todo_data: TodoCreate, db:Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud.create_todo(db,todo_data,current_user)


@router.put("/{todo_id}", response_model=TodoOut)
def todo_update(todo_id: int, todo_data: TodoUpdate,db:Session=Depends(get_db),current_user: User = Depends(get_current_user)):
    todo = crud.get_todo_by_id(db,todo_id,current_user.id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return crud.update_todo(db,todo,todo_data)

@router.delete("/{todo_id}", status_code= status.HTTP_204_NO_CONTENT)
def todo_delete(todo_id:int,db:Session = Depends(get_db),current_user:User=Depends(get_current_user)):
    todo = crud.get_todo_by_id(db, todo_id, current_user.id)
    if not todo:
        raise HTTPException(status_code=404, detail="To-do not found")
    crud.delete_todo(db, todo)
    return None

