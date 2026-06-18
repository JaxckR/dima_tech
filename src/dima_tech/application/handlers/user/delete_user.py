from dataclasses import dataclass

from dima_tech.application.ports import TransactionManager, IdentityProvider
from dima_tech.application.ports.repositories import UserRepository
from dima_tech.domain.entities.user import UserId, Role


@dataclass(slots=True, frozen=True)
class DeleteUserHandler:
    _user_repository: UserRepository
    _transaction_manager: TransactionManager
    _identity_provider: IdentityProvider

    async def handle(self, user_id: UserId) -> None:
        await self._identity_provider.access_only(Role.ADMIN)
        await self._user_repository.delete(user_id)
        await self._transaction_manager.commit()
