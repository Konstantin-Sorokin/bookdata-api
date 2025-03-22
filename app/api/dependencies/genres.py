from typing import Annotated

from fastapi import Path, Depends, HTTPException, status, Body

from models import Genre
from services import get_genre_service, GenreService
from schemas.genre import GenreCreate, GenreUpdate, GenrePartialUpdate


async def get_all_genres_dep(
    genre_service: Annotated[GenreService, Depends(get_genre_service)],
) -> list[Genre]:
    return await genre_service.get_all_genres()


async def get_genre_by_id_dep(
    genre_id: Annotated[int, Path],
    genre_service: Annotated[GenreService, Depends(get_genre_service)],
) -> Genre:
    genre = await genre_service.get_genre_by_id(genre_id=genre_id)
    if genre is not None:
        return genre

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Genre {genre_id} not found!",
    )


async def create_genre_dep(
    genre_in: Annotated[GenreCreate, Body],
    genre_service: Annotated[GenreService, Depends(get_genre_service)],
) -> Genre:
    return await genre_service.create_genre(genre_in=genre_in)


async def update_genre_dep(
    genre: Annotated[Genre, Depends(get_genre_by_id_dep)],
    genre_update: Annotated[GenreUpdate, Body],
    genre_service: Annotated[GenreService, Depends(get_genre_service)],
) -> Genre:
    return await genre_service.update_genre(
        genre=genre,
        genre_update=genre_update,
    )


async def update_genre_partial_dep(
    genre: Annotated[Genre, Depends(get_genre_by_id_dep)],
    genre_update: Annotated[GenrePartialUpdate, Body],
    genre_service: Annotated[GenreService, Depends(get_genre_service)],
) -> Genre:
    return await genre_service.update_genre(
        genre=genre,
        genre_update=genre_update,
        partial=True,
    )
