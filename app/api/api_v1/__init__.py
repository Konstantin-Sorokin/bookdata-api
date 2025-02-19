from fastapi import APIRouter

from app.utils.config import settings
from .public import router as public_router
from .admin import router as admin_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(public_router)
router.include_router(admin_router)
