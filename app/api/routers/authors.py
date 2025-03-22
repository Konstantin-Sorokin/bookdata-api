from typing import Annotated, Any
from fastapi import APIRouter, Depends, status

from api.dependencies.authors import (
    get_author_by_id_dep,
    get_author_with_bio_dep,
    get_authors_by_name_dep,
    create_author_dep,
    update_author_dep,
    update_author_partial_dep,
)
from schemas.author import AuthorRead, AuthorReadBio
from utils.config import settings
from models import Author

router = APIRouter(
    tags=["Authors"],
    prefix=settings.api.authors_prefix,
)


@router.get(
    "/{author_id}/",
    response_model=AuthorRead,
    status_code=status.HTTP_200_OK,
)
async def get_author_by_id(
    author: Annotated[Author, Depends(get_author_by_id_dep)],
) -> Any:
    return author


@router.get(
    "/{author_id}/bio",
    response_model=AuthorReadBio,
    status_code=status.HTTP_200_OK,
)
async def get_author_with_bio(
    author: Annotated[Author, Depends(get_author_with_bio_dep)],
) -> Any:
    return author


@router.get(
    "/",
    response_model=list[AuthorRead],
    status_code=status.HTTP_200_OK,
)
async def get_authors_by_name(
    authors: Annotated[list[Author], Depends(get_authors_by_name_dep)],
) -> Any:
    return authors


@router.post(
    "/",
    response_model=AuthorRead,
    status_code=status.HTTP_201_CREATED,
    include_in_schema=settings.api.show_admin_endpoints,
)
async def create_author(
    author: Annotated[Author, Depends(create_author_dep)],
) -> Any:
    return author


@router.put(
    "/{author_id}/",
    response_model=AuthorRead,
    status_code=status.HTTP_200_OK,
    include_in_schema=settings.api.show_admin_endpoints,
)
async def update_author(
    author: Annotated[Author, Depends(update_author_dep)],
) -> Any:
    return author


@router.patch(
    "/{author_id}/",
    response_model=AuthorRead,
    status_code=status.HTTP_200_OK,
    include_in_schema=settings.api.show_admin_endpoints,
)
async def update_author_partial(
    author: Annotated[Author, Depends(update_author_partial_dep)],
) -> Any:
    return author
