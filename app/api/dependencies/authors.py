from typing import Annotated

from fastapi import Path, Depends, HTTPException, status, Body, Query

from models import Author
from services import get_author_service, AuthorService
from schemas.author import AuthorCreate, AuthorUpdate, AuthorPartialUpdate


async def get_author_by_id_dep(
    author_id: Annotated[int, Path],
    author_service: Annotated[AuthorService, Depends(get_author_service)],
) -> Author:
    author: Author | None = await author_service.get_author_by_id(author_id=author_id)
    if author is not None:
        return author

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Author {author_id} not found!",
    )


async def get_author_with_bio_dep(
    author_id: Annotated[int, Path],
    author_service: Annotated[AuthorService, Depends(get_author_service)],
) -> Author:
    author: Author | None = await author_service.get_author_with_bio(
        author_id=author_id
    )
    if author is not None:
        return author

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Author {author_id} not found!",
    )


async def get_authors_by_name_dep(
    name: Annotated[str, Query],
    author_service: Annotated[AuthorService, Depends(get_author_service)],
) -> list[Author]:
    return await author_service.get_authors_by_name(name=name)


async def create_author_dep(
    author_in: Annotated[AuthorCreate, Body],
    author_service: Annotated[AuthorService, Depends(get_author_service)],
) -> Author:
    return await author_service.create_author(author_in=author_in)


async def update_author_dep(
    author: Annotated[Author, Depends(get_author_by_id_dep)],
    author_update: Annotated[AuthorUpdate, Body],
    author_service: Annotated[AuthorService, Depends(get_author_service)],
) -> Author:
    return await author_service.update_author(
        author=author,
        author_update=author_update,
    )


async def update_author_partial_dep(
    author: Annotated[Author, Depends(get_author_by_id_dep)],
    author_update: Annotated[AuthorPartialUpdate, Body],
    author_service: Annotated[AuthorService, Depends(get_author_service)],
) -> Author:
    return await author_service.update_author(
        author=author,
        author_update=author_update,
        partial=True,
    )
