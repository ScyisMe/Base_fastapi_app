from typing import TYPE_CHECKING, Annotated

from fastapi import Depends
from core.model import User
from core.model.db_helper import db_helper

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession



async def get_user_db(session: Annotated["AsyncSession", Depends(db_helper.session_getter)]):
    yield User.get_db(session)

