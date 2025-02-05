from typing import TYPE_CHECKING

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, relationship, mapped_column

from .base import Base
from .mixins import IdPkMixin

if TYPE_CHECKING:
    from .author import Author
    from .genre import Genre


class Book(IdPkMixin, Base):

    title: Mapped[str] = mapped_column(String(50))
    description: Mapped[str | None] = mapped_column(Text)
    publication_year: Mapped[int | None]

    authors: Mapped[list["Author"]] = relationship(
        secondary="book_author_association",
        back_populates="books",
    )
    genres: Mapped[list["Genre"]] = relationship(
        secondary="book_genre_association",
        back_populates="books",
    )
