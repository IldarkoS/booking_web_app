from pydantic import BaseModel, Field
from datetime import date

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
        orm_mode = True

class SBookingsResponse(BaseModel):
    Bookings: SBookings = Field()