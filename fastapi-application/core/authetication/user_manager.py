import logging
from typing import Optional, TYPE_CHECKING

from fastapi import Depends
from fastapi_users import BaseUserManager
from core.model.mixin.id_prim_key import IdIntPrimMixin

from core.config import setting
from core.types.user_id import UserIdType
from core.model import User

from core.model.db_helper import db_helper

if TYPE_CHECKING:
    from fastapi import Request


log = logging.getLogger(__name__)

class UserManager(IdIntPrimMixin, BaseUserManager[User, UserIdType]):
    
    reset_password_token_secret = setting.access_token.reset_password_token_secret
    verification_token_secret = setting.access_token.verification_token_secret
    
    def parse_id(self, id: str) -> UserIdType:
        return int(id)
    
    async def on_after_request_verify(
        self, user: User, token: str, request: Optional["Request"] = None
    ):
        log.warning("Verification requested for user %r. Verification token: %r", user.id, token)


    async def on_after_register(self, user: User, request: Optional["Request"] = None):
        log.warning("User %r has registered.", user.id)

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional["Request"] = None
    ):
        log.warning("User %r has forgot their password. Reset token: %r", user.id, token)


async def get_user_manager(user_db=Depends(db_helper.session_getter)):
    yield UserManager(user_db)