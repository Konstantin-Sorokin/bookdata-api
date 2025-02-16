from fastapi import APIRouter

from app.utils.config import settings
from .public import router as public_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(
    public_router,
)
