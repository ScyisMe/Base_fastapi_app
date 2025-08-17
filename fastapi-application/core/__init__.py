from pydantic import BaseModel

class UserShema(BaseModel):
    username: str