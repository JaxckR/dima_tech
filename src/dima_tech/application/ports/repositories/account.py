from abc import abstractmethod
from decimal import Decimal
from typing import Protocol

from dima_tech.domain.entities.account import Account, AccountId
from dima_tech.domain.entities.user import UserId


class AccountRepository(Protocol):
    @abstractmethod
    def add(self, instance: Account) -> None: ...

    @abstractmethod
    async def get_by_user_id(self, user_id: UserId) -> list[Account]: ...

    @abstractmethod
    async def get(self, id_: AccountId) -> Account | None: ...

    @abstractmethod
    async def increase_balance(self, id_: AccountId, amount: Decimal) -> None: ...
