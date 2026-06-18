from dataclasses import dataclass

from dima_tech.application.exceptions import NotFoundError
from dima_tech.application.ports import TransactionManager, IdentityProvider
from dima_tech.application.ports.repositories import UserRepository
from dima_tech.domain.entities.user import Role, UserId, FullName


@dataclass(slots=True, frozen=True)
class UpdateUserRequest:
    email: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    patronymic: str | None = None
    role: Role | None = None


@dataclass(slots=True, frozen=True)
class UpdateUserHandler:
    _user_repository: UserRepository
    _transaction_manager: TransactionManager
    _identity_provider: IdentityProvider

    async def handle(self, user_id: UserId, request: UpdateUserRequest) -> None:
        await self._identity_provider.access_only(Role.ADMIN)
        user = await self._user_repository.get(user_id)

        if user is None:
            raise NotFoundError()

        if request.email:
            user.email = request.email
        if request.role:
            user.role = request.role

        if request.first_name or request.last_name or request.patronymic:
            user.full_name = FullName(
                first_name=request.first_name or user.full_name.first_name,
                last_name=request.last_name or user.full_name.last_name,
                patronymic=request.patronymic or user.full_name.patronymic,
            )

        await self._transaction_manager.commit()
