from fastapi import APIRouter

from .fastapi_users import fastapi_users
from core.config import setting
from core.shemas.user import UserRead, UserUpdate


router =  APIRouter(
    prefix=setting.api.v1.users,
    tags=["Users"],
)

router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
)