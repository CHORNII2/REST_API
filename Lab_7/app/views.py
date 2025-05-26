from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from app.models import SECRET_KEY, ALGORITHM
from app.schemas import Book

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

books_db = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "Brave New World", "author": "Aldous Huxley"},
]

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.get("/books")
def get_books(user: str = Depends(get_current_user)):
    return books_db
