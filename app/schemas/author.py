from pydantic import BaseModel

from .mixins import ConfigDictMixin, IdMixin


class AuthorBase(BaseModel):
    name_ru: str
    name_en: str


class AuthorRead(ConfigDictMixin, IdMixin, AuthorBase):
    pass


# TODO: Временно закомментировано.
# class AuthorReadBooks(AuthorRead):
#     """Схема: автор с книгами"""
#
#     pass
#
#
# class AuthorReadBio(AuthorRead):
#     """Схема: автор с биографией"""
#
#     pass
#
#
# class AuthorReadFull(AuthorRead):
#     """Схема: автор с книгами и биографией"""
#
#     pass


class AuthorCreate(AuthorBase):
    pass


class AuthorUpdate(AuthorCreate):
    pass


class AuthorPartialUpdate(AuthorCreate):
    name_ru: str | None = None
    name_en: str | None = None
