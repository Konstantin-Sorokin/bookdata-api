from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, relationship, mapped_column

from models.base import Base
from models.mixins import IdPkMixin

if TYPE_CHECKING:
    from models.biography import Biography
    from models.book import Book


class Author(IdPkMixin, Base):

    name_ru: Mapped[str] = mapped_column(String(100))
    name_en: Mapped[str] = mapped_column(String(100))

    biography: Mapped["Biography"] = relationship(back_populates="author")

    books: Mapped[list["Book"]] = relationship(
        secondary="book_author_association",
        back_populates="authors",
    )
