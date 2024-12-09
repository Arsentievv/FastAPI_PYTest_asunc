from src.data_base.session_manager import Base
from sqlalchemy.orm import Mapped, mapped_column
from src.utils.fields import created_at, updated_at


class Material(Base):
    __tablename__ = "materials"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    materials_type: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str | None] = mapped_column(nullable=False)
    photo: Mapped[str | None] = mapped_column(nullable=True)

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
