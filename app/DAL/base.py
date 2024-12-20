from app.database import async_session_maker

from sqlalchemy import select, insert, delete

class BaseDAL:
    model = None

    @classmethod
    async def get_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def get_one_or_none(cls, **parameters):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**parameters)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def get_all(cls, **parameters):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**parameters)
            result = await session.execute(query)
            # return result.mappings().all()
            return result.scalars().all()

    @classmethod
    async def create_new(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete(cls, **parameters):
        async with async_session_maker() as session:
            query = delete(cls.model).filter_by(**parameters)
            await session.execute(query)
            await session.commit()