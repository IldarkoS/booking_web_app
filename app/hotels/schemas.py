from pydantic import BaseModel
from typing import Optional, List


class SHotels(BaseModel):
    id: int
    name: str
    location: str
    services: list
    rooms_quantity: int
    image_id: int

    class Config:
        orm_mode = True


class SHotelsInfo(SHotels):
    id: int
    name: str
    location: str
    services: list
    rooms_quantity: int
    image_id: int
    rooms_left: int

    class Config:
        orm_mode = True


class SRooms(BaseModel):
    id: int
    hotel_id: int
    name: str
    description: Optional[str]
    services: List[str]
    price: int
    quantity: int
    image_id: int

    class Config:
        orm_mode = True

class SRoomsInfo(SRooms):
    total_cost: int
    rooms_left: int

    class Config:
        orm_mode = True