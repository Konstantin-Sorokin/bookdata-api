from typing import Annotated

from fastapi import Path, Depends, HTTPException, status, Body
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Book
from app.utils import db_helper
from app.crud import book as book_crud
from app.schemas.book import BookCreate


async def get_book_by_id(
    book_id: Annotated[int, Path],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> Book:
    book = await book_crud.get_book_by_id(session=session, book_id=book_id)
    if book is not None:
        return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book {book_id} not found!",
    )


async def create_book(
    book_in: Annotated[BookCreate, Body],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> Book:
    return await book_crud.create_book(session=session, book_in=book_in)
