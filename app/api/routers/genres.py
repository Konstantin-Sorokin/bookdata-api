from typing import Annotated
from fastapi import APIRouter, Depends, status

from api.dependencies.genres import (
    get_all_genres_dep,
    get_genre_by_id_dep,
    create_genre_dep,
    update_genre_dep,
    update_genre_partial_dep,
)
from app.schemas.genre import GenreRead
from app.utils.config import settings
from app.models import Genre

router = APIRouter(
    tags=["Genres"],
    prefix=settings.api.genres_prefix,
)


@router.get(
    "/",
    response_model=list[GenreRead],
    status_code=status.HTTP_200_OK,
)
async def get_all_genres(
    genres: Annotated[list[Genre], Depends(get_all_genres_dep)],
):
    return genres


@router.get(
    "/{genre_id}/",
    response_model=GenreRead,
    status_code=status.HTTP_200_OK,
)
async def get_genre(
    genre: Annotated[Genre, Depends(get_genre_by_id_dep)],
):
    return genre


@router.post(
    "/",
    response_model=GenreRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_genre(
    genre: Annotated[Genre, Depends(create_genre_dep)],
):
    return genre


@router.put(
    "/{genre_id}/",
    response_model=GenreRead,
    status_code=status.HTTP_200_OK,
)
async def update_genre(
    genre: Annotated[Genre, Depends(update_genre_dep)],
):
    return genre


@router.patch(
    "/{genre_id}/",
    response_model=GenreRead,
    status_code=status.HTTP_200_OK,
)
async def update_genre(
    genre: Annotated[Genre, Depends(update_genre_partial_dep)],
):
    return genre
