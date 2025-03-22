from pydantic import BaseModel

from schemas.mixins import ConfigDictMixin, IdMixin
from schemas.author import AuthorRead
from schemas.genre import GenreRead


class BookBase(BaseModel):
    """
    Схема книги базовая

    Поля:
        title (str)
    """

    title: str


class BookReadMin(ConfigDictMixin, IdMixin, BookBase):
    """
    Схема получения минимальных данных книги

    Поля:
        id (int)
        title (str)
    """

    pass


class BookPreviewRead(BookReadMin):
    """
    Схема получения данных для превью книги

    Поля:
        id (int)
        title (str)
        authors (list[AuthorRead])
    """

    authors: list[AuthorRead]


class BookFullRead(BookPreviewRead):
    """
    Схема получения всех данных книги

    Поля:
        id (int)
        title (str)
        description (str | None)
        publication_year (int | None)
        authors (list[AuthorRead])
        genres (list[GenreRead])
    """

    description: str | None = None
    publication_year: int | None = None
    genres: list[GenreRead]


class BookCreate(BookBase):
    """
    Схема для создания книги

    Поля:
        title (str)
        description (str | None)
        publication_year (int | None)
    """

    description: str | None = None
    publication_year: int | None = None


class BookUpdate(BookCreate):
    """
    Схема для полного обновления книги

    Поля:
        title (str)
        description (str | None)
        publication_year (int | None)
    """

    pass


class BookPartialUpdate(BookCreate):
    """
    Схема для частичного обновления книги

    Поля:
        title (str | None)
        description (str | None)
        publication_year (int | None)
    """

    title: str | None = None
