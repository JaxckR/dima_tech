from decimal import Decimal

from sqlalchemy import select, update

from dima_tech.application.ports.repositories import AccountRepository
from dima_tech.domain.entities.account import Account, AccountId
from dima_tech.domain.entities.user import UserId
from dima_tech.infrastructure.persistence.adapters.common import SQLAMixin


class AccountRepositoryImpl(SQLAMixin, AccountRepository):
    async def increase_balance(self, id_: AccountId, amount: Decimal) -> None:
        await self._session.execute(
            update(Account)
            .where(Account.id == id_)
            .values(balance=Account.balance + amount)
        )

    def add(self, instance: Account) -> None:
        self._session.add(instance)

    async def get(self, id_: AccountId) -> Account | None:
        query = await self._session.execute(select(Account).where(Account.id == id_))
        return query.scalar_one_or_none()

    async def get_by_user_id(self, user_id: UserId) -> list[Account]:
        query = await self._session.execute(
            select(Account).where(Account.user_id == user_id)
        )
        return list(query.scalars().all())
