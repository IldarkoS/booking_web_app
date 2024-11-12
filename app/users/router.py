from fastapi import APIRouter, HTTPException, status, Response, Depends

from app.database import async_session_maker
from app.users.schemas import SUserAuth
from app.users.DAL import UsersDAL
from app.users.auth import get_password_hash, verify_password, authenticate_user, create_access_token
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/auth",
    tags=["Аунтефикация и Пользователи"]
)


@router.post("/register")
async def register_user(user_data: SUserAuth):
    existing_user = await UsersDAL.get_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=400)
    hashed_password = get_password_hash(user_data.password)
    await UsersDAL.create_new(email=user_data.email, hashed_password=hashed_password)


@router.post("/login")
async def register_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("booking_access_token", access_token, httponly=True)
    return {"access_token": access_token}

@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("booking_access_token")
    return {"success":"user logout"}


@router.get("/about")
async def get_user_info(user: Users = Depends(get_current_user)):
    return user