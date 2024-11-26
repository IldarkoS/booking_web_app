from fastapi import FastAPI, Query
from typing import Optional
from datetime import date
from pydantic import BaseModel

from fastapi import FastAPI, Request, Response
from fastapi_redis_cache import FastApiRedisCache, cache
from sqlalchemy.orm import Session

from app.bookings.router import router as bookings_router
from app.users.router import router as users_router
from app.hotels.router import router as hotels_router
from app.config import settings

app = FastAPI()

app.include_router(users_router)
app.include_router(bookings_router)
app.include_router(hotels_router)


@app.on_event("startup")
def startup():
    redis_cache = FastApiRedisCache()
    redis_cache.init(
        host_url=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
        prefix="cache",
        response_header="X-MyAPI-Cache",
        ignore_arg_types=[Request, Response, Session]
    )