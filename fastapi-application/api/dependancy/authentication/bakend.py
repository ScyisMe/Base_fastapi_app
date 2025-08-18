from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy

from core.authetication.transport import barer_transport
from .strategy import get_database_strategy

authentication_backend = AuthenticationBackend(
    name="access-tokens-db",
    transport=barer_transport,
    get_strategy=get_database_strategy,
    
)