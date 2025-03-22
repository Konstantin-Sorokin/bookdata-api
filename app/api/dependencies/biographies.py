from typing import Annotated

from fastapi import Path, Depends, HTTPException, status, Body

from models import Biography
from services import get_biography_service, BiographyService
from schemas.biography import BiographyCreate, BiographyUpdate, BiographyPartialUpdate


async def get_biography_by_id_dep(
    biography_id: Annotated[int, Path],
    biography_service: Annotated[BiographyService, Depends(get_biography_service)],
) -> Biography:
    biography = await biography_service.get_biography_by_id(biography_id=biography_id)
    if biography is not None:
        return biography

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Biography {biography_id} not found!",
    )


async def create_biography_dep(
    biography_in: Annotated[BiographyCreate, Body],
    biography_service: Annotated[BiographyService, Depends(get_biography_service)],
) -> Biography:
    return await biography_service.create_biography(biography_in=biography_in)


async def update_biography_dep(
    biography: Annotated[Biography, Depends(get_biography_by_id_dep)],
    biography_update: Annotated[BiographyUpdate, Body],
    biography_service: Annotated[BiographyService, Depends(get_biography_service)],
) -> Biography:
    return await biography_service.update_biography(
        biography=biography,
        biography_update=biography_update,
    )


async def update_biography_partial_dep(
    biography: Annotated[Biography, Depends(get_biography_by_id_dep)],
    biography_update: Annotated[BiographyPartialUpdate, Body],
    biography_service: Annotated[BiographyService, Depends(get_biography_service)],
) -> Biography:
    return await biography_service.update_biography(
        biography=biography,
        biography_update=biography_update,
        partial=True,
    )
