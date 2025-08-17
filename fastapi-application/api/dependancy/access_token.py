from typing import TYPE_CHECKING, Annotated

from fastapi import Depends
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
)
from core.model.db_helper import db_helper
from core.model import AccessToken

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

async def get_access_token_db(
    session: Annotated["AsyncSession", Depends(db_helper.session_getter)],
):  
    yield AccessToken.get_db(session)