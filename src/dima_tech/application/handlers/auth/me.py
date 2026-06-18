from dataclasses import dataclass

from dima_tech.application.dto import UserDTO
from dima_tech.application.exceptions import ApplicationError
from dima_tech.application.ports import IdentityProvider
from dima_tech.application.ports.repositories import UserRepository


@dataclass(slots=True, frozen=True)
class MeHandler:
    _user_repository: UserRepository
    _identity_provider: IdentityProvider

    async def handle(self) -> UserDTO:
        user_id = await self._identity_provider.get_user_id()

        if user_id is None:
            raise ApplicationError()

        user = await self._user_repository.get(user_id)

        if user is None:
            raise ApplicationError()

        return UserDTO.from_entity(user)
