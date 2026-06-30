from sqlalchemy import BigInteger, String, TEXT, ForeignKey
from sqlalchemy.orm import Mapped,mapped_column, relationship

from app.models.base import BaseTimeStamp

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.boards.models import Board


class Post(BaseTimeStamp):

    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
    )

    title: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    contents: Mapped[str] = mapped_column(
        TEXT
    )

    board_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey(
            "boards.id",
            name="fk_posts_boards"
        ),
        nullable=False,
    )

    board: Mapped['Board'] = relationship(
        "Board",
        back_populates="posts",
    )



