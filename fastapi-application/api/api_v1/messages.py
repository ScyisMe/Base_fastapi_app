from fastapi import APIRouter
from fastapi import Depends
from typing import Annotated

from core.config import setting
from core.model import User
from .fastapi_users import current_user, current_superuser
from core.shemas.user import UserRead

router = APIRouter(prefix=setting.api.v1.messages,
                   tags=["Messages"])

@router.get("",)
def get_user_messages(
    user: Annotated[User, Depends(current_user)]
):
    return {
        "messages": ["m1", "m2", "m3"],
        "user": UserRead.model_validate(user),
    }

@router.get("/secrets")
def get_superuser_messages(
    user: Annotated[User, Depends(current_superuser)]
):
    return {
        "messages": ["secret-m1", "secret-m2", "secret-m3"],
        "user": UserRead.model_validate(user),
    }