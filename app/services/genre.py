from typing import Annotated

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from models import Genre
from schemas.genre import GenreCreate, GenreUpdate, GenrePartialUpdate
from utils import db_helper
from services.base import BaseService


class GenreService(BaseService):

    async def get_all_genres(self) -> list[Genre]:
        stmt = select(Genre).order_by(Genre.name)
        genres = await self.session.scalars(stmt)
        return list(genres)

    async def get_genre_by_id(self, genre_id: int) -> Genre | None:
        return await self.session.get(Genre, genre_id)

    async def create_genre(self, genre_in: GenreCreate) -> Genre:
        genre = Genre(**genre_in.model_dump())
        self.session.add(genre)
        await self.session.commit()
        return genre

    async def update_genre(
        self,
        genre: Genre,
        genre_update: GenreUpdate | GenrePartialUpdate,
        partial: bool = False,
    ) -> Genre:
        for name, value in genre_update.model_dump(exclude_unset=partial).items():
            setattr(genre, name, value)
        await self.session.commit()
        return genre


def get_genre_service(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> GenreService:
    """
    Возвращает экземпляр GenreService с переданной сессией.
    """
    return GenreService(session=session)
