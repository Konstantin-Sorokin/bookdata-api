from typing import Annotated

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from models import Book, Genre, BookAuthorAssociation, BookGenreAssociation, Author
from schemas.book import BookCreate, BookUpdate, BookPartialUpdate
from utils import db_helper
from services.base import BaseService


class BookService(BaseService):

    async def get_book_by_id(self, book_id: int) -> Book | None:
        return await self.session.get(Book, book_id)

    async def get_books_by_name(self, name: str) -> list[Book]:
        stmt = select(Book).where(Book.title.ilike(f"%{name}%"))
        books = await self.session.scalars(stmt)
        return list(books)

    async def get_books_by_genre(self, genre_id: int) -> list[Book]:
        stmt = select(Book).join(Book.genres).where(Genre.id == genre_id)
        books = await self.session.scalars(stmt)
        return list(books)

    async def get_books_by_author(self, author_id: int) -> list[Book]:
        stmt = select(Book).join(Book.authors).where(Author.id == author_id)
        books = await self.session.scalars(stmt)
        return list(books)

    async def create_book(self, book_in: BookCreate) -> Book:
        book = Book(**book_in.model_dump())
        self.session.add(book)
        await self.session.commit()
        return book

    async def update_book(
        self,
        book: Book,
        book_update: BookUpdate | BookPartialUpdate,
        partial: bool = False,
    ) -> Book:
        for name, value in book_update.model_dump(exclude_unset=partial).items():
            setattr(book, name, value)
        await self.session.commit()
        return book

    async def associate_book_with_authors(
        self, book_id: int, author_ids: list[int]
    ) -> None:
        for author_id in author_ids:
            association = BookAuthorAssociation(book_id=book_id, author_id=author_id)
            self.session.add(association)

        await self.session.commit()

    async def associate_book_with_genres(
        self, book_id: int, genre_ids: list[int]
    ) -> None:
        for genre_id in genre_ids:
            association = BookGenreAssociation(book_id=book_id, genre_id=genre_id)
            self.session.add(association)

        await self.session.commit()


def get_book_service(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> BookService:
    """
    Возвращает экземпляр BookService с переданной сессией.
    """
    return BookService(session=session)
