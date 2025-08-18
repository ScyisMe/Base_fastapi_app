from core.types.user_id import UserIdType
from fastapi_users import FastAPIUsers

from api.dependancy.authentication.depends_user_maneger import get_user_manager
from api.dependancy.authentication.bakend import authenticationbackend
from core.model.user import User

fastapi_users = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [authenticationbackend],
)