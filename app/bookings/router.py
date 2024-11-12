from fastapi import APIRouter

from app.database import async_session_maker
from app.bookings.DAL import BookingsDAL

from app.bookings.schemas import SBookings, SBookingsResponse


router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"]
)


@router.get("")
async def get_bookings() -> list[SBookings]:
    async with async_session_maker() as session:
        return await BookingsDAL.get_all()