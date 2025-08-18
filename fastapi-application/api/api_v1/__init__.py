from fastapi import APIRouter

from core.config import setting

from .auth import router as auth_router

router = APIRouter(prefix=setting.api.v1.prefix)

router.include_router(
    auth_router,
)

