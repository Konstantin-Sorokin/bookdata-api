from typing import Annotated, Union

from fastapi import Path, Depends, HTTPException, status, Body
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Book
from app.utils import db_helper
from app.crud import book as book_crud
from app.schemas.book import BookCreate, BookUpdate, BookPartialUpdate


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


async def update_book(
    book: Annotated[Book, Depends(get_book_by_id)],
    book_update: Annotated[BookUpdate, Body],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> Book:
    return await book_crud.update_book(
        session=session,
        book=book,
        book_update=book_update,
    )


async def update_book_partial(
    book: Annotated[Book, Depends(get_book_by_id)],
    book_update: Annotated[BookPartialUpdate, Body],
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> Book:
    return await book_crud.update_book(
        session=session,
        book=book,
        book_update=book_update,
        partial=True,
    )
