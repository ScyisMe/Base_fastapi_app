from collections.abc import AsyncGenerator
from typing import TYPE_CHECKING

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTable,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, ForeignKey

from core.types.user_id import UserIdType
from model.base import Base

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    
class AccessToken(SQLAlchemyBaseAccessTokenTable[UserIdType], Base):  
    user_id: Mapped[UserIdType] = mapped_column(
        Integer,
        ForeignKey("users.id", ondelete="cascade"),
        nullable=False,
    )
    @classmethod
    def get_db(cls, session:"AsyncSession"):
        return  SQLAlchemyAccessTokenDatabase(session, cls)