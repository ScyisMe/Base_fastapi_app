from collections.abc import AsyncGenerator
from typing import TYPE_CHECKING

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.orm import DeclarativeBase

from .base import Base
from .mixin.id_prim_key import IdIntPrimMixin

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

class User(Base, IdIntPrimMixin, SQLAlchemyBaseUserTable[int]):
    @classmethod
    def get_db(cls, session: AsyncSession):
        return SQLAlchemyUserDatabase(session, User)