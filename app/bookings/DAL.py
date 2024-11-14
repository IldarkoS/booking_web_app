from sqlalchemy import select, and_, or_, func, insert, delete
from datetime import date

from app.database import async_session_maker
from app.bookings.models import Bookings
from app.rooms.models import Rooms
from app.DAL.base import BaseDAL


class BookingsDAL(BaseDAL):
    model = Bookings

    @classmethod
    async def create_new(
        cls,
        user_id: int,
        room_id: int,
        date_from: date,
        date_to: date,
        ):
        '''add new booking if rooms available'''
        async with async_session_maker() as session:
            booked_rooms = select(Bookings).where(
                and_(
                    Bookings.room_id == room_id,
                    or_(
                        and_(
                            Bookings.date_from >=  date_from, 
                            Bookings.date_from <= date_to
                        ),
                        and_(
                            Bookings.date_from <= date_from,
                            Bookings.date_to > date_from 
                        )
                    )
                )
            ).cte("booked_rooms")

            rooms_left = select(
                (Rooms.quantity - func.count(booked_rooms.c.room_id))
                ).select_from(Rooms).join(
                    booked_rooms, booked_rooms.c.room_id == Rooms.id, isouter=True
                ).where(
                    Rooms.id == room_id
                ).group_by(
                    Rooms.quantity, booked_rooms.c.room_id
                )

            rooms_left = await session.execute(rooms_left)
            rooms_left: int = rooms_left.scalar()

            if rooms_left > 0:
                get_price = select(Rooms.price).filter_by(id=room_id)
                price = await session.execute(get_price)
                price: int = price.scalar()
                add_booking = insert(Bookings).values(
                    room_id=room_id,
                    user_id=user_id,
                    date_from=date_from,
                    date_to=date_to,
                    price=price
                ).returning(Bookings)
                new = await session.execute(add_booking)
                await session.commit()
                return new.scalar()
            else:
                return None


    @classmethod
    async def get_all(
        cls, 
        user_id: int
    ):
        async with async_session_maker() as session:
            '''select * from bookings b 
                left join rooms r on b.room_id = r.id
                where user_id = 3'''

            get_bookings = select(
                Bookings.__table__.columns,
                Rooms.__table__.columns
            ).join(
                Rooms, Rooms.id == Bookings.room_id, isouter=True
            ).where(
                Bookings.user_id == user_id
            )

            result = await session.execute(get_bookings)
            return result.mappings().all()

    