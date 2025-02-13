from typing import TYPE_CHECKING

from pydantic import BaseModel

from .mixins import ConfigDictMixin, IdMixin

if TYPE_CHECKING:
    from .author import AuthorRead
    from .genre import GenreRead


class BookBase(BaseModel):
    title: str
    description: str | None = None
    publication_year: int | None = None


class BookRead(ConfigDictMixin, IdMixin, BookBase):
    authors: list["AuthorRead"]
    genres: list["GenreRead"]


class BookCreate(BookBase):
    pass


class BookUpdate(BookCreate):
    pass


class BookPartialUpdate(BookCreate):
    title: str | None = None
