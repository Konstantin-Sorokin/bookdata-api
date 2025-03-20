from typing import Annotated

from fastapi import Path, Depends, HTTPException, status, Body

from app.models import Book
from app.services import get_book_service, BookService
from app.schemas.book import BookCreate, BookUpdate, BookPartialUpdate, BookReadMin


async def get_book_by_id_dep(
    book_id: Annotated[int, Path],
    book_service: Annotated[BookService, Depends(get_book_service)],
) -> Book:
    book: Book | None = await book_service.get_book_by_id(book_id=book_id)
    if book is not None:
        return book

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book {book_id} not found!",
    )


async def create_book_dep(
    book_in: Annotated[BookCreate, Body],
    book_service: Annotated[BookService, Depends(get_book_service)],
) -> Book:
    return await book_service.create_book(book_in=book_in)


async def update_book_dep(
    book: Annotated[Book, Depends(get_book_by_id_dep)],
    book_update: Annotated[BookUpdate, Body],
    book_service: Annotated[BookService, Depends(get_book_service)],
) -> Book:
    return await book_service.update_book(
        book=book,
        book_update=book_update,
    )


async def update_book_partial_dep(
    book: Annotated[Book, Depends(get_book_by_id_dep)],
    book_update: Annotated[BookPartialUpdate, Body],
    book_service: Annotated[BookService, Depends(get_book_service)],
) -> Book:
    return await book_service.update_book(
        book=book,
        book_update=book_update,
        partial=True,
    )
