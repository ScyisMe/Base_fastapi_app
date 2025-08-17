from fastapi import APIRouter

from core.config import setting

from .users import router as user_router

router = APIRouter(prefix=setting.api.v1.prefix)

router.include_router(
    user_router,
    prefix=setting.api.v1.users,
)

