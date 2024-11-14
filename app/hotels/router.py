from fastapi import APIRouter
from datetime import date

from app.database import async_session_maker
from app.hotels.DAL import HotelsDAL
from app.hotels.schemas import SHotels, SRoomsInfo, SHotelsInfo


router = APIRouter(
    prefix="/hotels",
    tags=["Отели"]
)


@router.get("")
async def get_hotels(
    location: str,
    date_from: date,
    date_to: date
) -> list[SHotelsInfo]:
    return await HotelsDAL.get_all(location, date_from, date_to)


@router.get("/{hotel_id}/rooms")
async def get_hotel_rooms(
    hotel_id: int,
    date_from: date,
    date_to: date
    ) -> list[SRoomsInfo]:
    return await HotelsDAL.hotel_rooms(hotel_id, date_from, date_to)


@router.get("/id/{hotel_id}")
async def get_hotel_info(
    hotel_id: int
) -> SHotels:
    return await HotelsDAL.get_one_or_none(id=hotel_id)