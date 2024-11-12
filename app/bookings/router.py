from fastapi import APIRouter, Request, Depends

from app.database import async_session_maker
from app.bookings.DAL import BookingsDAL
from app.users.models import Users
from app.users.dependencies import get_current_user

from app.bookings.schemas import SBookings, SBookingsResponse


router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"]
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBookings]:
    return await BookingsDAL.get_all(user_id=user.id)


