from sqlalchemy import BigInteger, String, TEXT
from sqlalchemy.orm import Mapped,mapped_column

from app.models.base import BaseTimeStamp

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






