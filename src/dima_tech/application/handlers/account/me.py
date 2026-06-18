from dataclasses import dataclass

from dima_tech.application.exceptions import AccessError
from dima_tech.application.ports import IdentityProvider
from dima_tech.application.ports.repositories import AccountRepository
from dima_tech.domain.entities.account import Account


@dataclass(slots=True, frozen=True)
class MeAccountHandler:
    _account_repository: AccountRepository
    _identity_provider: IdentityProvider

    async def handle(self) -> list[Account]:
        user_id = await self._identity_provider.get_user_id()

        if user_id is None:
            raise AccessError()

        return await self._account_repository.get_by_user_id(user_id)
