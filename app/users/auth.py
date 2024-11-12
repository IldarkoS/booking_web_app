from passlib.context import CryptContext
from jose import jwt
from datetime import timedelta, datetime
from pydantic import EmailStr

from app.users.DAL import UsersDAL
from app.config import settings

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=1)
    to_encode.update(
        {
            "exp":expire,
        }
    )
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, settings.ALGORITHM
    )
    return encoded_jwt

async def authenticate_user(email: EmailStr, password: str):
    user = await UsersDAL.get_one_or_none(email=email)
    if not user and not verify_password(password, user.password):
        return None
    return user