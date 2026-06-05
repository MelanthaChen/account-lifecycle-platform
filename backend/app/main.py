from fastapi import FastAPI

from app.core.config import settings

from app.api.v1.account_routes import router as account_router
from app.api.v1.activity_routes import router as activity_router
from app.api.v1.dashboard_routes import router as dashboard_router
from app.api.v1.scheduler_routes import router as scheduler_router


app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
)


app.include_router(account_router)
app.include_router(activity_router)
app.include_router(dashboard_router)
app.include_router(scheduler_router)


@app.get("/")
def health():
    return {
        "status": "running",
        "project": settings.PROJECT_NAME,
    }