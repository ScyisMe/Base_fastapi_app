from fastapi import APIRouter

from .fastapi_users import fastapi_users
from core.config import setting
from api.dependancy.authentication.bakend import authentication_backend

router =  APIRouter(
    prefix=setting.api.v1.auth,
    tags=["Auth"],
)

router.include_router(
    fastapi_users.get_auth_router(authentication_backend),
    prefix="/jwt",
    )