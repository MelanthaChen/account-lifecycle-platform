from app.database.session import SessionLocal
from app.repositories.account_repository import AccountRepository
from app.schemas.account import AccountCreate


db = SessionLocal()

account = AccountRepository.create(
    db,
    AccountCreate(
        platform="reddit",
        username="mel123",
        email="mel123@test.com",
    ),
)

print(account.id)
print(account.username)