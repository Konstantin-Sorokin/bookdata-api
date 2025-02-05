from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import IdPkMixin


class BookAuthorAssociation(IdPkMixin, Base):
    __table_args__ = (
        UniqueConstraint(
            "book_id",
            "author_id",
            name="idx_unique_book_author",
        ),
    )

    book_id: Mapped[int] = mapped_column(ForeignKey("book.id"))
    author_id: Mapped[int] = mapped_column(ForeignKey("author.id"))
