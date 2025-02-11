from pydantic import BaseModel, ConfigDict


class BookBase(BaseModel):
    username: str


class BookCreate(BookBase):
    pass


class BookRead(BookBase):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int