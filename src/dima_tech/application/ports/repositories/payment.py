from abc import abstractmethod
from typing import Protocol

from dima_tech.domain.entities.payment import Payment
from dima_tech.domain.entities.user import UserId


class PaymentRepository(Protocol):
    @abstractmethod
    async def get_by_user_id(self, user_id: UserId) -> list[Payment]: ...

    @abstractmethod
    def add(self, instance: Payment) -> None: ...
