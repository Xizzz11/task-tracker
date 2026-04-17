from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.security import decode_access_token
from app.repositories.user_repository import UserRepository
from app.db.models.user import User

oauth2_scheme = ... (перенеси из security или оставь здесь)

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    # ... логика как в оригинале
    pass

def get_current_admin(current_user: User = Depends(get_current_user)):
    # ...
    pass