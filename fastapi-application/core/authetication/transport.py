from fastapi_users.authentication import BearerTransport

barer_transport = BearerTransport(tokenUrl="auth/user/loggin")