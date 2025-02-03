from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from .base import Base
from .mixins.id_pk import IdPkMixin

if TYPE_CHECKING:
    from .biography import Biography


class Author(IdPkMixin, Base):

    name_ru: Mapped[str]
    name_en: Mapped[str]

    biography: Mapped["Biography"] = relationship(back_populates="author")
