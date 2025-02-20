from fastapi import APIRouter

from app.utils.config import settings
from .books import router as books_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(books_router)
