from typing import Annotated

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from models import Biography
from schemas.biography import BiographyCreate, BiographyUpdate, BiographyPartialUpdate
from utils import db_helper
from services.base import BaseService


class BiographyService(BaseService):

    async def get_biography_by_id(self, biography_id: int) -> Biography | None:
        return await self.session.get(Biography, biography_id)

    async def create_biography(self, biography_in: BiographyCreate) -> Biography:
        biography = Biography(**biography_in.model_dump())
        self.session.add(biography)
        await self.session.commit()
        return biography

    async def update_biography(
        self,
        biography: Biography,
        biography_update: BiographyUpdate | BiographyPartialUpdate,
        partial: bool = False,
    ) -> Biography:
        for name, value in biography_update.model_dump(exclude_unset=partial).items():
            setattr(biography, name, value)
        await self.session.commit()
        return biography


def get_biography_service(
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
) -> BiographyService:
    """
    Возвращает экземпляр BiographyService с переданной сессией.
    """
    return BiographyService(session=session)
