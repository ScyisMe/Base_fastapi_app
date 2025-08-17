from collections.abc import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from .base import Base
from .mixin.id_prim_key import IdIntPrimMixin

class User(Base, IdIntPrimMixin, SQLAlchemyBaseUserTable[int]):
    pass