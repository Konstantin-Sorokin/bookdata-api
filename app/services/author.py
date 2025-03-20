from typing import Annotated

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from app.models import Author, Biography
from app.schemas.author import AuthorCreate, AuthorUpdate, AuthorPartialUpdate
from app.utils import db_helper
from app.services.base import BaseService


class AuthorService(BaseService):

    async def get_author_by_id(
        self,
        author_id: int,
    ) -> Author | None:
        return await self.session.get(Author, author_id)

    async def create_author(self, author_in: AuthorCreate) -> Author:
        author = Author(**author_in.model_dump())
        self.session.add(author)
        await self.session.commit()
        return author

    async def get_author_with_bio(self, author_id: int) -> Author: ...

    async def get_author_with_books(self, author_id: int) -> Author: ...


def get_author_service(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> AuthorService:
    """
    Возвращает экземпляр AuthorService с переданной сессией.
    """
    return AuthorService(session=session)
