from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.user import UserRepository
from app.core.security import verify_password, create_access_token

class AuthService:
    def __init__(self, db: Session):
        self.db = db
        self.repo = UserRepository(db)

    def register(self, username: str, email: str, password: str):
        if self.repo.get_by_username(username) or self.repo.get_by_email(email):
            raise HTTPException(status_code=400, detail="Username or email already registered")
        return self.repo.create(username, email, password)

    def login(self, username: str, password: str):
        user = self.repo.get_by_username(username)
        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password"
            )
        access_token = create_access_token({"sub": user.username})
        return {"access_token": access_token, "token_type": "bearer"}