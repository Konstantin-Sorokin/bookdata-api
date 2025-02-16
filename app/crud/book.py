from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Book


async def get_book(session: AsyncSession, book_id: int) -> Book | None:
    return await session.get(Book, book_id)
