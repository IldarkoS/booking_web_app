from fastapi import APIRouter, Request, Depends, HTTPException, status
from datetime import date

from app.database import async_session_maker
from app.bookings.DAL import BookingsDAL
from app.users.models import Users
from app.users.dependencies import get_current_user

from app.bookings.schemas import SBookings, SBookingsInfo


router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"]
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBookingsInfo]:
    return await BookingsDAL.get_all(user_id=user.id)


@router.post("")
async def add_booking(
    room_id: int,
    date_from: date,
    date_to: date,
    user: Users = Depends(get_current_user)
    ): 
    booking = await BookingsDAL.create_new(user.id, room_id, date_from, date_to)
    if not booking:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Нет свободных номеров")
    else:
        return booking


@router.delete("/{id}")
async def delete_booking(
    booking_id: int,
    user: Users = Depends(get_current_user)
):
    await BookingsDAL.delete(id=booking_id, user_id=user.id)