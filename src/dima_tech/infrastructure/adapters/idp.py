from dataclasses import dataclass

from starlette.requests import Request

from dima_tech.application.exceptions import AccessError
from dima_tech.application.ports import IdentityProvider, Clock
from dima_tech.application.ports.repositories import SessionRepository, UserRepository
from dima_tech.domain.entities.session import SessionId
from dima_tech.domain.entities.user import Role, UserId


@dataclass
class IdentityProviderImpl(IdentityProvider):
    _request: Request
    _clock: Clock
    _session_repository: SessionRepository
    _user_repository: UserRepository

    def get_session_id(self) -> SessionId | None:
        if session := self._request.cookies.get("session_id"):
            return SessionId(session)
        return None

    async def get_user_id(self) -> UserId | None:
        session_id = self.get_session_id()

        if session_id is None:
            return None

        session = await self._session_repository.get(session_id)

        if not session or session.expires_at < self._clock.now():
            return None

        return session.user_id

    async def access_only(self, role: Role) -> None:
        user_id = await self.get_user_id()

        if user_id is None:
            raise AccessError()

        user = await self._user_repository.get(user_id)

        if user is None or user.role < role:
            raise AccessError()
