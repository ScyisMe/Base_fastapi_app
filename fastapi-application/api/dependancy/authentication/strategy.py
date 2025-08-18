from fastapi import Depends
from fastapi_users.authentication.strategy.db import AccessTokenDatabase, DatabaseStrategy

from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from core.model import AccessToken
    
from core.config import setting
from .access_token import get_access_token_db

def get_database_strategy(
    access_token_db: Annotated[AccessTokenDatabase["AccessToken"], Depends(get_access_token_db)],
) -> DatabaseStrategy:
    return DatabaseStrategy(access_token_db, lifetime_seconds=setting.access_token.lifetime_seconds)