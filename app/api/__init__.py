from fastapi import APIRouter

from app.utils.config import settings
from .routers import router as router_api


router = APIRouter(
    prefix=settings.api.prefix,
)

router.include_router(
    router=router_api,
)
