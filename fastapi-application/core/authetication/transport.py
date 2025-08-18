from fastapi_users.authentication import BearerTransport

from core.config import setting

barer_transport = BearerTransport(tokenUrl=setting.api.barer_token_url) 