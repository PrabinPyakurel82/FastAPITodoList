from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session

from core.db import get_db
from core.security import hash_password

from schemas import UserCreate, UserOut
from models import User


router = APIRouter(prefix='/auth', tags=['auth'])

@router.post("/register", response_model=UserOut)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter_by(email = user_data.email).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="User with this email exists.")
    
    new_user = User(
        full_name=user_data.full_name,
        email= user_data.email,
        hashed_password=hash_password(user_data.password))
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user