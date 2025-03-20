from typing import Annotated, Any
from fastapi import APIRouter, Depends, status

from api.dependencies.books import (
    get_book_by_id_dep,
    create_book_dep,
    update_book_dep,
    update_book_partial_dep,
)
from app.schemas.book import BookReadMin
from app.utils.config import settings
from app.models import Book

router = APIRouter(
    tags=["Books"],
    prefix=settings.api.v1.books_prefix,
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


@router.post(
    "/",
    response_model=BookReadMin,
    status_code=status.HTTP_201_CREATED,
    include_in_schema=settings.api.v1.show_admin_endpoints,
)
async def create_book(
    book: Annotated[Book, Depends(create_book_dep)],
) -> Any:
    return book


@router.put(
    "/{product_id}/",
    response_model=BookReadMin,
    status_code=status.HTTP_200_OK,
    include_in_schema=settings.api.v1.show_admin_endpoints,
)
async def update_book(
    book: Annotated[Book, Depends(update_book_dep)],
) -> Any:
    return book


@router.patch(
    "/{product_id}/",
    response_model=BookReadMin,
    status_code=status.HTTP_200_OK,
    include_in_schema=settings.api.v1.show_admin_endpoints,
)
async def update_book_partial(
    book: Annotated[Book, Depends(update_book_partial_dep)],
) -> Any:
    return book
