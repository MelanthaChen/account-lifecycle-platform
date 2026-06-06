from sqlalchemy.orm import Session

from app.repositories.account_repository import AccountRepository
from app.schemas.account import AccountCreate


class AccountService:

    @staticmethod
    def create_account(
        db: Session,
        account_data: AccountCreate,
    ):
        return AccountRepository.create(
            db,
            account_data,
        )

    @staticmethod
    def get_all_accounts(
        db: Session,
    ):
        return AccountRepository.get_all(db)

    @staticmethod
    def get_account_by_id(
        db: Session,
        account_id: int,
    ):
        return AccountRepository.get_by_id(
            db,
            account_id,
        )