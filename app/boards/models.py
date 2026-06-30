from app.models.base import BaseTimeStamp

from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from app.posts.models import Post


class Board(BaseTimeStamp):

    __tablename__ = 'boards'

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    posts: Mapped[List['Post']] = relationship(
        "Post",
        back_populates="board",
    )


