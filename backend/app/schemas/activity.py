from datetime import datetime

from pydantic import BaseModel


class ActivityCreate(BaseModel):
    account_id: int
    activity_type: str
    notes: str = ""


class ActivityResponse(BaseModel):
    id: int
    account_id: int
    activity_type: str
    status: str
    notes: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }