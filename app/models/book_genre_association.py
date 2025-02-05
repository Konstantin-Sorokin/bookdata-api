from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import IdPkMixin


class BookGenreAssociation(IdPkMixin, Base):
    __table_args__ = (
        UniqueConstraint(
            "book_id",
            "genre_id",
            name="idx_unique_book_genre",
        ),
    )

    book_id: Mapped[int] = mapped_column(ForeignKey("book.id"))
    genre_id: Mapped[int] = mapped_column(ForeignKey("genre.id"))
