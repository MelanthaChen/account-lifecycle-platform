from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.account import (
    AccountCreate,
    AccountResponse,
)

from app.services.account_service import AccountService


router = APIRouter(
    prefix="/accounts",
    tags=["Accounts"],
)


@router.post(
    "/",
    response_model=AccountResponse,
)
def create_account(
    account_data: AccountCreate,
    db: Session = Depends(get_db),
):
    return AccountService.create_account(
        db,
        account_data,
    )


@router.get(
    "/",
    response_model=list[AccountResponse],
)
def get_accounts(
    db: Session = Depends(get_db),
):
    return AccountService.get_all_accounts(db)


@router.get(
    "/{account_id}",
    response_model=AccountResponse,
)
def get_account(
    account_id: int,
    db: Session = Depends(get_db),
):
    return AccountService.get_account_by_id(
        db,
        account_id,
    )