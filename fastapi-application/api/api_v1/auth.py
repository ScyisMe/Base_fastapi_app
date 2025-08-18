from fastapi import APIRouter

from .fastapi_users import fastapi_users
from core.config import setting
from api.dependancy.authentication.bakend import authentication_backend
from core.shemas.user import UserRead, UserCreate

router =  APIRouter(
    prefix=setting.api.v1.auth,
    tags=["Auth"],
)

# /loggin
# /logout
router.include_router(
    fastapi_users.get_auth_router(authentication_backend),
    )

# /register
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
)

# /verify
router.include_router(
    fastapi_users.get_verify_router(UserRead),
) 

router.include_router(
    fastapi_users.get_reset_password_router()
)