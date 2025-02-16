from fastapi import APIRouter, Depends

from app.api.api_v1.dependencies.books import book_by_id
from app.schemas.book import BookReadMin
from app.utils.config import settings

router = APIRouter(
    tags=["Products"],
    prefix=settings.api.v1.books,
)


@router.get("/{book_id}/", response_model=BookReadMin)
async def get_book(
    book: BookReadMin = Depends(book_by_id),
):
    return book
