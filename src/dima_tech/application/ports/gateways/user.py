from abc import abstractmethod
from typing import Protocol

from dima_tech.application.dto import UserWithAccountsDTO


class UserGateway(Protocol):
    @abstractmethod
    async def get_all_with_accounts(self) -> list[UserWithAccountsDTO]: ...
