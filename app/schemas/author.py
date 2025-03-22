from pydantic import BaseModel

from schemas.mixins import ConfigDictMixin, IdMixin
from schemas.biography import BiographyBase


class AuthorBase(BaseModel):
    """
    Схема автора базовая

    Поля:
        name_ru (str)
        name_en (str)
    """

    name_ru: str
    name_en: str


class AuthorRead(ConfigDictMixin, IdMixin, AuthorBase):
    """
    Схема получения базовых данных автора

    Поля:
        id (int)
        name_ru (str)
        name_en (str)
    """

    pass


class AuthorReadBio(AuthorRead):
    """
    Схема получения данных автора и его биографии

    Поля:
        id (int)
        name_ru (str)
        name_en (str)
        biography (BiographyBase)
    """

    biography: BiographyBase


class AuthorCreate(AuthorBase):
    """
    Схема для создания автора

    Поля:
        name_ru (str)
        name_en (str)
    """

    pass


class AuthorUpdate(AuthorCreate):
    """
    Схема для полного обновления автора

    Поля:
        name_ru (str)
        name_en (str)
    """

    pass


class AuthorPartialUpdate(AuthorCreate):
    """
    Схема для частичного обновления автора

    Поля:
        name_ru (str | None)
        name_en (str | None)
    """

    name_ru: str | None = None
    name_en: str | None = None
