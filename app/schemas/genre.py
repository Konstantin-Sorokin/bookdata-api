from pydantic import BaseModel

from schemas.mixins import ConfigDictMixin, IdMixin


class GenreBase(BaseModel):
    """
    Схема жанра базовая

    Поля:
        name (str): название жанра на русском
        slug (str): английское название жанра
    """

    name: str
    slug: str


class GenreRead(ConfigDictMixin, IdMixin, GenreBase):
    """
    Схема получения данных жанра

    Поля:
        id (int)
        name (str): название жанра на русском
        slug (str): английское название жанра
    """

    pass


class GenreCreate(GenreBase):
    """
    Схема для создания жанра

    Поля:
        name (str): название жанра на русском
        slug (str): английское название жанра
    """

    pass


class GenreUpdate(GenreCreate):
    """
    Схема для полного обновления жанра

    Поля:
        name (str): название жанра на русском
        slug (str): английское название жанра
    """

    pass


class GenrePartialUpdate(GenreCreate):
    """
    Схема для частичного обновления жанра

    Поля:
        name (str | None): название жанра на русском
        slug (str | None): английское название жанра
    """

    name: str | None = None
    slug: str | None = None
