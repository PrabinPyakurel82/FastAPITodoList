from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session


from core.db import get_db
from models import User
from core.security import ALGORITHM, SECRET_KEY


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(token:str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    user_id: str = payload.get('sub')

    if user_id is None:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
           detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
     
    user = db.query(User).filter(User.id == int(user_id)).first()
    if user is None:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
           detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return user