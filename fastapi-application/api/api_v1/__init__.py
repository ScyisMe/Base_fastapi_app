from fastapi import APIRouter
from fastapi import Depends
from fastapi.security import HTTPBearer

from core.config import setting

from .auth import router as auth_router
from .users import router as user_router
from .messages import router as message_router

http_bearer = HTTPBearer(auto_error=False)

router = APIRouter(
    prefix=setting.api.v1.prefix,
    dependencies=[Depends(http_bearer)]
    )

router.include_router(
    auth_router,
)

router.include_router(
    user_router,
)
router.include_router(
    router=message_router,
)