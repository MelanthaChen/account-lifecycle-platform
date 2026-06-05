from fastapi import APIRouter

router = APIRouter(
    prefix="/scheduler",
    tags=["Scheduler"],
)


@router.get("/")
def scheduler():
    return {"message": "scheduler route"}