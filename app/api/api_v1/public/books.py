from typing import Annotated
from fastapi import APIRouter, Depends

from app.api.api_v1.dependencies.books import get_book_by_id
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
