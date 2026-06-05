from datetime import datetime

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    platform: Mapped[str] = mapped_column(
        String(100),
        index=True,
    )

    username: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="active",
    )

    created_at: Mapped[datetime] = mapped_column(
        default=datetime.utcnow
    )