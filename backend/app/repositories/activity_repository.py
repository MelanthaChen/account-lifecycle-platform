from sqlalchemy.orm import Session

from app.models.activity_log import ActivityLog
from app.schemas.activity import ActivityCreate


class ActivityRepository:

    @staticmethod
    def create(
        db: Session,
        activity_data: ActivityCreate,
    ) -> ActivityLog:

        activity = ActivityLog(
            account_id=activity_data.account_id,
            activity_type=activity_data.activity_type,
            notes=activity_data.notes,
        )

        db.add(activity)

        db.commit()

        db.refresh(activity)

        return activity

    @staticmethod
    def get_all(
        db: Session,
    ):
        return (
            db.query(ActivityLog)
            .order_by(ActivityLog.created_at.desc())
            .all()
        )

    @staticmethod
    def get_by_account_id(
        db: Session,
        account_id: int,
    ):
        return (
            db.query(ActivityLog)
            .filter(
                ActivityLog.account_id == account_id
            )
            .order_by(
                ActivityLog.created_at.desc()
            )
            .all()
        )