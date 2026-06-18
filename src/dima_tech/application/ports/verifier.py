from abc import abstractmethod
from typing import Protocol

from dima_tech.domain.entities.account import AccountId
from dima_tech.domain.entities.payment import TransactionId
from dima_tech.domain.entities.user import UserId


class Verifier(Protocol):
    @abstractmethod
    def verify_password(self, password: str, hashed_password: str) -> bool: ...

    @abstractmethod
    def verify_transaction(
        self,
        transaction_id: TransactionId,
        account_id: AccountId,
        user_id: UserId,
        amount: str,
        signature: str,
    ) -> bool: ...
