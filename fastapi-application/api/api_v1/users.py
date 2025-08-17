from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import ORJSONResponse

from core.crud import get_all_users, create_user_db
from core.shemas.user import UserRead, UserCreate
from core.model.db_helper import db_helper

router = APIRouter(tags=["Users"], default_response_class=ORJSONResponse)

@router.get("", response_model=list[UserRead])
async def get_user(
    session: Annotated[AsyncSession,Depends(db_helper.session_getter)],
):
    users = await get_all_users(session=session)
    return users

@router.post("", response_model=UserRead)
async def create_user(
    user: UserCreate,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
): 
    user = await create_user_db(
        user_create=user,
        session=session,
        )
    return user