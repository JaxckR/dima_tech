from dataclasses import dataclass

from dima_tech.application.dto import UserWithAccountsDTO
from dima_tech.application.ports import IdentityProvider
from dima_tech.application.ports.gateways import UserGateway
from dima_tech.domain.entities.user import Role


@dataclass(slots=True, frozen=True)
class GetAllUsersHandler:
    _user_gateway: UserGateway
    _identity_provider: IdentityProvider

    async def handle(self) -> list[UserWithAccountsDTO]:
        await self._identity_provider.access_only(Role.ADMIN)
        return await self._user_gateway.get_all_with_accounts()
