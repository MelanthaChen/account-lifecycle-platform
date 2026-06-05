from fastapi import APIRouter

router = APIRouter(
    prefix="/activities",
    tags=["Activities"],
)


@router.get("/")
def get_activities():
    return {"message": "activities route"}