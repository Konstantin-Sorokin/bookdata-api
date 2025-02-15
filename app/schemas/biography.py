from pydantic import BaseModel
from datetime import date

from .mixins import ConfigDictMixin, IdMixin


class BiographyBase(BaseModel):
    """
    Схема биографии базовая

    Поля:
        content (str): Текст биографии
        date_of_birth (date | None)
        date_of_death (date | None)
        nationality (str | None)
    """

    content: str
    date_of_birth: date | None = None
    date_of_death: date | None = None
    nationality: str | None = None


class BiographyRead(ConfigDictMixin, IdMixin, BiographyBase):
    """
    Схема получения всех данных биографии

    Поля:
        id (int)
        content (str)
        date_of_birth (date | None)
        date_of_death (date | None)
        nationality (str | None)
    """

    pass


class BiographyCreate(BiographyBase):
    """
    Схема для создания биографии

    Поля:
        content (str)
        date_of_birth (date | None)
        date_of_death (date | None)
        nationality (str | None)
    """

    pass


class BiographyUpdate(BiographyCreate):
    """
    Схема для полного обновления биографии

    Поля:
        content (str)
        date_of_birth (date | None)
        date_of_death (date | None)
        nationality (str | None)
    """

    pass


class BiographyPartialUpdate(BiographyCreate):
    """
    Схема для частичного обновления биографии
    Поля:
        content (str | None)
        date_of_birth (date | None)
        date_of_death (date | None)
        nationality (str | None)
    """

    content: str | None = None
