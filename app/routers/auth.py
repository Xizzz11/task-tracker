from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import get_current_user
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.user import UserCreate, UserOut, Token
from app.services.auth_service import AuthService


router = APIRouter()

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return AuthService(db).register(user.username, user.email, user.password)

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Нужно импортировать OAuth2PasswordRequestForm из fastapi.security
    from fastapi.security import OAuth2PasswordRequestForm
    # (в реальном коде импортируй вверху)
    return AuthService(db).login(form_data.username, form_data.password)

@router.get("/me", response_model=UserOut)
def read_users_me(current_user=Depends(get_current_user)):
    return current_user