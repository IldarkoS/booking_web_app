from pydantic import BaseModel, Field
from datetime import date
from typing import List, Optional

class SBookings(BaseModel):
    id: int 
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    total_days: int

    class Config:
        from_attributes = True

# class SBookingsResponse(BaseModel):
#     Bookings: SBookings = Field()


class SBookingsInfo(SBookings):
    image_id: int
    name: str
    description: Optional[str]
    services: List[str]

    class Config:
        from_attributes = True