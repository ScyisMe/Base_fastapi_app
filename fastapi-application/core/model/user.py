from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixin.int_id_primary import IntIdPkMixin

class User(IntIdPkMixin, Base):
    username: Mapped[str] = mapped_column(unique=True)