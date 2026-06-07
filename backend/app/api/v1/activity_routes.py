from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.activity import (
    ActivityCreate,
    ActivityResponse,
)

from app.services.activity_service import (
    ActivityService,
)


router = APIRouter(
    prefix="/activities",
    tags=["Activities"],
)


@router.post(
    "/",
    response_model=ActivityResponse,
)
def create_activity(
    activity_data: ActivityCreate,
    db: Session = Depends(get_db),
):
    return ActivityService.create_activity(
        db,
        activity_data,
    )


@router.get(
    "/",
    response_model=list[ActivityResponse],
)
def get_activities(
    db: Session = Depends(get_db),
):
    return ActivityService.get_all_activities(
        db,
    )


@router.get(
    "/account/{account_id}",
    response_model=list[ActivityResponse],
)
def get_account_activities(
    account_id: int,
    db: Session = Depends(get_db),
):
    return ActivityService.get_account_activities(
        db,
        account_id,
    )