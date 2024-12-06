from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime


class MaterialBase(BaseModel):
    title: str = Field(
        max_length=40, description="Название"
    )
    description: str = Field(
        default=None, max_length=500, description="Описание"
    )
    photo: HttpUrl = Field(
        default=None, description="Изображение"
    )
    created_at: datetime = Field(
        description="Дата создания"
    )
    updated_at: datetime = Field(
        description="Дата обновления"
    )
