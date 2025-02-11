from pydantic import BaseModel

from .mixins import ConfigDictMixin


class AuthorBase(BaseModel):
    name_ru: str

class AuthorRead(ConfigDictMixin, AuthorBase):

    id: int

class AuthorCreate(AuthorBase):
    pass


class AuthorUpdate(AuthorCreate):
    pass


