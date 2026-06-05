from sqlalchemy.orm import Session

from app.models.account import Account
from app.schemas.account import AccountCreate


class AccountRepository:

    @staticmethod
    def create(
        db: Session,
        account_data: AccountCreate,
    ) -> Account:

        account = Account(
            platform=account_data.platform,
            username=account_data.username,
            email=account_data.email,
        )

        db.add(account)

        db.commit()

        db.refresh(account)

        return account

    @staticmethod
    def get_all(
        db: Session,
    ):
        return db.query(Account).all()

    @staticmethod
    def get_by_id(
        db: Session,
        account_id: int,
    ):
        return (
            db.query(Account)
            .filter(Account.id == account_id)
            .first()
        )