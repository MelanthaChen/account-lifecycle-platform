from datetime import datetime

from pydantic import BaseModel
from pydantic import EmailStr


class AccountCreate(BaseModel):
    platform: str
    username: str
    email: EmailStr


class AccountResponse(BaseModel):
    id: int
    platform: str
    username: str
    email: str
    status: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }