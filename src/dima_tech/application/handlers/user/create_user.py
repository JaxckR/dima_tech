from dataclasses import dataclass

from dima_tech.application.factories.user import UserFactory
from dima_tech.application.ports import TransactionManager, IdentityProvider
from dima_tech.application.ports.repositories import UserRepository
from dima_tech.domain.entities.user import Role


@dataclass(slots=True, frozen=True)
class CreateUserRequest:
    email: str
    password: str
    first_name: str
    last_name: str
    patronymic: str | None = None
    role: Role = Role.USER


@dataclass(slots=True, frozen=True)
class CreateUserHandler:
    _user_factory: UserFactory
    _user_repository: UserRepository
    _transaction_manager: TransactionManager
    _identity_provider: IdentityProvider

    async def handle(self, request: CreateUserRequest) -> None:
        await self._identity_provider.access_only(Role.ADMIN)
        user = await self._user_factory.create(
            email=request.email,
            password=request.password,
            first_name=request.first_name,
            last_name=request.last_name,
            patronymic=request.patronymic,
            role=request.role,
        )
        self._user_repository.add(user)
        await self._transaction_manager.commit()
