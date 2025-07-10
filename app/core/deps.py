from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session


from db import get_db
from models import User
from security import ALGORITHM, SECRET_KEY


def get_current_user(token:str = Depends(OAuth2PasswordBearer), db: Session = Depends(get_db)):
    payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    user_id: str = payload.get('sub')

    if user_id is None:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
           detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
     
    user = db.query(User).get(User.id == user.id)
    if user is None:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
           detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return user