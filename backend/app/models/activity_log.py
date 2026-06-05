from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base


class ActivityLog(Base):
    __tablename__ = "activity_logs"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    account_id: Mapped[int] = mapped_column(
        ForeignKey("accounts.id"),
        index=True,
    )

    activity_type: Mapped[str] = mapped_column(
        String(100),
        index=True,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="success",
    )

    notes: Mapped[str] = mapped_column(
        String(1000),
        default="",
    )

    created_at: Mapped[datetime] = mapped_column(
        default=datetime.utcnow,
        index=True,
    )