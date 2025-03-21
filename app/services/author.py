from typing import Annotated

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from sqlalchemy.orm import joinedload, selectinload

from models import Author
from schemas.author import AuthorCreate, AuthorUpdate, AuthorPartialUpdate
from utils import db_helper
from services.base import BaseService


class AuthorService(BaseService):

    async def get_author_by_id(self, author_id: int) -> Author | None:
        return await self.session.get(Author, author_id)

    async def get_authors_by_name(self, name: str) -> list[Author]:
        stmt = select(Author).where(Author.name_ru.ilike(f"%{name}%"))
        authors = await self.session.scalars(stmt)
        return list(authors)

    async def get_author_with_bio(self, author_id: int) -> Author:
        stmt = (
            select(Author)
            .options(joinedload(Author.biography))
            .where(Author.id == author_id)
        )
        author = await self.session.scalar(stmt)
        return author

    async def get_author_with_books(self, author_id: int) -> Author:
        stmt = (
            select(Author)
            .options(selectinload(Author.books))
            .where(Author.id == author_id)
        )
        author = await self.session.scalar(stmt)
        return author

    async def create_author(self, author_in: AuthorCreate) -> Author:
        author = Author(**author_in.model_dump())
        self.session.add(author)
        await self.session.commit()
        return author

    async def update_author(
        self,
        author: Author,
        author_update: AuthorUpdate | AuthorPartialUpdate,
        partial: bool = False,
    ) -> Author:
        for name, value in author_update.model_dump(exclude_unset=partial).items():
            setattr(author, name, value)
        await self.session.commit()
        return author


def get_author_service(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> AuthorService:
    """
    Возвращает экземпляр AuthorService с переданной сессией.
    """
    return AuthorService(session=session)
