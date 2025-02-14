from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import IdPkMixin

if TYPE_CHECKING:
    from .book import Book


class Genre(IdPkMixin, Base):

    name: Mapped[str] = mapped_column(String(30), unique=True)
    slug: Mapped[str] = mapped_column(String(30), unique=True)

    books: Mapped[list["Book"]] = relationship(
        secondary="book_genre_association",
        back_populates="genres",
    )
