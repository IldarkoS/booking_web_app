from fastapi import APIRouter, Request

from app.database import async_session_maker
from app.bookings.DAL import BookingsDAL

from app.bookings.schemas import SBookings, SBookingsResponse


router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"]
)


@router.get("")
async def get_bookings(request: Request): #-> list[SBookings]:
    return await BookingsDAL.get_all()