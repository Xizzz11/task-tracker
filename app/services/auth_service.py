<<<<<<< HEAD
﻿from fastapi import HTTPException
from sqlalchemy.orm import Session

from app1.core.security import verify_password
from app1.repositories.user_repository import UserRepository
from app1.schemas.user import RegisterRequest


class AuthService:
    def __init__(self, db: Session):
        self.user_repo = UserRepository(db)

    def register_user(self, data: RegisterRequest):
        if self.user_repo.get_by_email(data.email):
            raise HTTPException(status_code=400, detail="Email already in use")
        if self.user_repo.get_by_username(data.username):
            raise HTTPException(status_code=400, detail="Username already in use")

        return self.user_repo.create(
            email=data.email,
            username=data.username,
            phone=data.phone,
            password=data.password,
        )

    def authenticate_user(self, login: str, password: str):
        user = self.user_repo.get_by_login(login)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user
=======
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
>>>>>>> f288b6a259cfa99c6d34b38d1f98492c44117b3c
