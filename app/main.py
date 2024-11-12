from fastapi import FastAPI, Query
from typing import Optional
from datetime import date
from pydantic import BaseModel

from app.bookings.router import router as bookings_router


app = FastAPI()

app.include_router(bookings_router)
