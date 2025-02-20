from typing import Union

from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Book
from app.schemas.book import BookCreate, BookUpdate, BookPartialUpdate


async def get_book_by_id(session: AsyncSession, book_id: int) -> Book | None:
    return await session.get(Book, book_id)


async def create_book(session: AsyncSession, book_in: BookCreate) -> Book:
    book = Book(**book_in.model_dump())
    session.add(book)
    await session.commit()
    return book


async def update_book(
    session: AsyncSession,
    book: Book,
    book_update: Union[BookUpdate, BookPartialUpdate],
    partial: bool = False,
) -> Book:
    for name, value in book_update.model_dump(exclude_unset=partial).items():
        setattr(book, name, value)
    await session.commit()
    return book
