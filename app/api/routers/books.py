from typing import Annotated, Any
from fastapi import APIRouter, Depends, status

from api.dependencies.books import (
    get_book_by_id_dep,
    search_books_dep,
    create_book_dep,
    update_book_dep,
    update_book_partial_dep,
)
from schemas.book import BookReadMin
from utils.config import settings
from models import Book

router = APIRouter(
    tags=["Books"],
    prefix=settings.api.books_prefix,
)


@router.get(
    "/{book_id}/",
    response_model=BookReadMin,
    status_code=status.HTTP_200_OK,
)
async def get_book_by_id(
    book: Annotated[Book, Depends(get_book_by_id_dep)],
) -> Any:
    return book


@router.get(
    "/",
    response_model=list[BookReadMin],
    status_code=status.HTTP_200_OK,
)
async def search_books(
    books: Annotated[list[Book], Depends(search_books_dep)],
) -> Any:
    return books


@router.post(
    "/",
    response_model=BookReadMin,
    status_code=status.HTTP_201_CREATED,
    include_in_schema=settings.api.show_admin_endpoints,
)
async def create_book(
    book: Annotated[Book, Depends(create_book_dep)],
) -> Any:
    return book


@router.put(
    "/{book_id}/",
    response_model=BookReadMin,
    status_code=status.HTTP_200_OK,
    include_in_schema=settings.api.show_admin_endpoints,
)
async def update_book(
    book: Annotated[Book, Depends(update_book_dep)],
) -> Any:
    return book


@router.patch(
    "/{book_id}/",
    response_model=BookReadMin,
    status_code=status.HTTP_200_OK,
    include_in_schema=settings.api.show_admin_endpoints,
)
async def update_book_partial(
    book: Annotated[Book, Depends(update_book_partial_dep)],
) -> Any:
    return book
