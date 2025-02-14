from pydantic import BaseModel

from .mixins import ConfigDictMixin, IdMixin


class GenreBase(BaseModel):
    name: str
    slug: str


class GenreRead(ConfigDictMixin, IdMixin, GenreBase):
    pass


class GenreCreate(GenreBase):
    pass


class GenreUpdate(GenreCreate):
    pass


class GenrePartialUpdate(GenreCreate):
    name: str | None = None
    slug: str | None = None
