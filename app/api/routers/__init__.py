from fastapi import APIRouter

from api.routers.books import router as books_router
from api.routers.genres import router as genres_router
from api.routers.authors import router as authors_router
from api.routers.biographies import router as biographies_router

router = APIRouter()

router.include_router(books_router)
router.include_router(genres_router)
router.include_router(authors_router)
router.include_router(biographies_router)
