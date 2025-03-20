from fastapi import APIRouter

from utils.config import settings
from api.routers import router as router_api


router = APIRouter(
    prefix=settings.api.prefix,
)

router.include_router(
    router=router_api,
)
