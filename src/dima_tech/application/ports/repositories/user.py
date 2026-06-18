from abc import abstractmethod
from typing import Protocol

from dima_tech.domain.entities.user import User, UserId


class UserRepository(Protocol):
    @abstractmethod
    def add(self, instance: User) -> None: ...

    @abstractmethod
    async def get(self, id_: UserId) -> User | None: ...

    @abstractmethod
    async def get_by_email(self, email: str) -> User | None: ...

    @abstractmethod
    async def delete(self, id_: UserId) -> None: ...
