from abc import abstractmethod
from typing import Protocol

from dima_tech.domain.entities.user import UserId, Role


class IdentityProvider(Protocol):
    @abstractmethod
    async def get_user_id(self) -> UserId | None: ...

    @abstractmethod
    async def access_only(self, role: Role) -> None: ...
