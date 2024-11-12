from app.database import async_session_maker
from sqlalchemy import select

from app.bookings.models import Bookings
from app.DAL.base import BaseDAL


class BookingsDAL(BaseDAL):
    model = Bookings