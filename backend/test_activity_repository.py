from app.database.session import SessionLocal

from app.repositories.activity_repository import (
    ActivityRepository,
)

from app.schemas.activity import ActivityCreate


db = SessionLocal()

activity = ActivityRepository.create(
    db,
    ActivityCreate(
        account_id=1,
        activity_type="browse",
        notes="Visited homepage",
    ),
)

print(activity.id)
print(activity.activity_type)