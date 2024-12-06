from data_base.session_manager import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime


class Material(Base):
    __tablename__ = "materials"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    photo: Mapped[str] = mapped_column(nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        default=datetime.utcnow(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        default_factory=datetime.utcnow, nullable=False
    )