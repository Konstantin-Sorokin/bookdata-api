from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Book
from app.schemas.book import BookCreate


async def get_book_by_id(session: AsyncSession, book_id: int) -> Book | None:
    return await session.get(Book, book_id)


async def create_book(session: AsyncSession, book_in: BookCreate) -> Book:
    book = Book(**book_in.model_dump())
    session.add(book)
    await session.commit()
    return book
