from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.user import UserOut
from app.repositories.user import UserRepository
from app.core.security import get_current_admin

router = APIRouter()

@router.get("/users", response_model=list[UserOut])
def get_all_users(db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    return UserRepository(db).get_all()