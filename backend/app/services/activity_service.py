from sqlalchemy.orm import Session

from app.repositories.activity_repository import (
    ActivityRepository,
)

from app.schemas.activity import ActivityCreate


class ActivityService:

    @staticmethod
    def create_activity(
        db: Session,
        activity_data: ActivityCreate,
    ):
        return ActivityRepository.create(
            db,
            activity_data,
        )

    @staticmethod
    def get_all_activities(
        db: Session,
    ):
        return ActivityRepository.get_all(
            db,
        )

    @staticmethod
    def get_account_activities(
        db: Session,
        account_id: int,
    ):
        return ActivityRepository.get_by_account_id(
            db,
            account_id,
        )