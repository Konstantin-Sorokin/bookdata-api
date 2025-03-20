from typing import Annotated

from fastapi import Path, Depends, HTTPException, status, Body, Query

from models import Book
from services import get_book_service, BookService
from schemas.book import BookCreate, BookUpdate, BookPartialUpdate, BookReadMin


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


async def search_books_dep(
    name: Annotated[str | None, Query] = None,
    author_id: Annotated[int | None, Query] = None,
    genre_id: Annotated[int | None, Query] = None,
    book_service: Annotated[BookService, Depends(get_book_service)] = None,
) -> list[Book]:
    if name is not None:
        return await book_service.get_books_by_name(name=name)
    if author_id is not None:
        return await book_service.get_books_by_author(author_id=author_id)
    if genre_id is not None:
        return await book_service.get_books_by_genre(genre_id=genre_id)

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Необходимо указать хотя бы один параметр для поиска (name, author_id, genre_id).",
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
