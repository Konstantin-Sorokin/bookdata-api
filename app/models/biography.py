from typing import TYPE_CHECKING

from sqlalchemy import Date, String, ForeignKey, Text
from sqlalchemy.orm import Mapped, relationship, mapped_column

from .base import Base
from .mixins import IdPkMixin

if TYPE_CHECKING:
    from .author import Author


class Biography(IdPkMixin, Base):
    __tablename__ = "biographies"

    content: Mapped[str] = mapped_column(Text, nullable=False)
    date_of_birth: Mapped[Date | None] = mapped_column(Date, nullable=True)
    date_of_death: Mapped[Date | None] = mapped_column(Date, nullable=True)
    nationality: Mapped[str | None] = mapped_column(String(30), nullable=True)

    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"), unique=True)
    author: Mapped["Author"] = relationship(back_populates="biography")
