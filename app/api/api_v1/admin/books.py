from typing import Annotated
from fastapi import APIRouter, Depends, status

from app.utils.config import settings
from app.api.api_v1.dependencies.books import (
    create_book,
    update_book,
    update_book_partial,
)
from app.schemas.book import BookReadMin

router = APIRouter(
    tags=["Books"],
    prefix=settings.api.v1.books,
)


@router.post(
    "/",
    response_model=BookReadMin,
    status_code=status.HTTP_201_CREATED,
)
async def create_book(
    book: Annotated[BookReadMin, Depends(create_book)],
) -> BookReadMin:
    return book


@router.put("/{product_id}/")
async def update_book(
    book: Annotated[BookReadMin, Depends(update_book)],
):
    return book


@router.patch("/{product_id}/")
async def update_book_partial(
    book: Annotated[BookReadMin, Depends(update_book_partial)],
):
    return book
