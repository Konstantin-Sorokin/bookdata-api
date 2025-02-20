from typing import Annotated
from fastapi import APIRouter, Depends, status

from .dependencies.books import (
    get_book_by_id,
    create_book,
    update_book,
    update_book_partial,
)
from app.schemas.book import BookReadMin
from app.utils.config import settings

router = APIRouter(
    tags=["Books"],
    prefix=settings.api.v1.books,
)


@router.get("/{book_id}/", response_model=BookReadMin)
async def get_book_by_id(
    book: Annotated[BookReadMin, Depends(get_book_by_id)],
) -> BookReadMin:
    return book


@router.post(
    "/",
    response_model=BookReadMin,
    status_code=status.HTTP_201_CREATED,
)
async def create_book(
    book: Annotated[BookReadMin, Depends(create_book)],
) -> BookReadMin:
    return book


@router.put(
    "/{product_id}/",
    response_model=BookReadMin,
    status_code=status.HTTP_200_OK,
)
async def update_book(
    book: Annotated[BookReadMin, Depends(update_book)],
) -> BookReadMin:
    return book


@router.patch(
    "/{product_id}/",
    response_model=BookReadMin,
    status_code=status.HTTP_200_OK,
)
async def update_book_partial(
    book: Annotated[BookReadMin, Depends(update_book_partial)],
) -> BookReadMin:
    return book
