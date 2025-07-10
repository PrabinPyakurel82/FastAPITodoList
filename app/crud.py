from datetime import datetime

from sqlalchemy.orm import Session

from models import Todo, User
from schemas import TodoCreate, TodoUpdate


def get_user_todos(db:Session,user_id: int):
    return db.query(Todo).filter(Todo.user_id == user_id).all()


def get_todo_by_id(db:Session,todo_id:int,user_id:int):
    return db.query(Todo).filter(Todo.id == todo_id ,Todo.user_id == user_id).first()

def create_todo(db: Session,todo_data: TodoCreate, user: User):
    new_todo = Todo(
        task=todo_data.task,
        completed=False,
        user_id=user.id,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


def update_todo(db:Session,todo:Todo,todo_data:TodoUpdate):
    if todo_data.task is not None:
        todo.task = todo_data.task
    
    if todo_data.completed is not None:
        todo.completed = todo_data.completed

    todo.updated_at = datetime.now()
    db.commit()
    db.refresh(todo)
    return todo


def delete_todo(db:Session, todo: Todo):
    db.delete(todo)
    db.commit()

