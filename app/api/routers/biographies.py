from typing import Annotated
from fastapi import APIRouter, Depends, status

from api.dependencies.biographies import (
    get_biography_by_id_dep,
    create_biography_dep,
    update_biography_dep,
    update_biography_partial_dep,
)
from schemas.biography import BiographyRead
from utils.config import settings
from models import Biography

router = APIRouter(
    tags=["Biographies"],
    prefix=settings.api.biographies_prefix,
)


@router.get(
    "/{biography_id}/",
    response_model=BiographyRead,
    status_code=status.HTTP_200_OK,
)
async def get_biography(
    biography: Annotated[Biography, Depends(get_biography_by_id_dep)],
):
    return biography


@router.post(
    "/",
    response_model=BiographyRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_biography(
    biography: Annotated[Biography, Depends(create_biography_dep)],
):
    return biography


@router.put(
    "/{biography_id}/",
    response_model=BiographyRead,
    status_code=status.HTTP_200_OK,
)
async def update_biography(
    biography: Annotated[Biography, Depends(update_biography_dep)],
):
    return biography


@router.patch(
    "/{biography_id}/",
    response_model=BiographyRead,
    status_code=status.HTTP_200_OK,
)
async def update_biography(
    biography: Annotated[Biography, Depends(update_biography_partial_dep)],
):
    return biography
