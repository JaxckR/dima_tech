from dataclasses import dataclass
from datetime import timedelta

from dima_tech.application.exceptions import NotFoundError, AccessError
from dima_tech.application.ports import (
    IdentityProvider,
    Verifier,
    IdGenerator,
    Clock,
    TransactionManager,
)
from dima_tech.application.ports.repositories import UserRepository, SessionRepository
from dima_tech.domain.entities.session import Session


@dataclass(slots=True, frozen=True)
class LoginRequest:
    email: str
    password: str


@dataclass(slots=True, frozen=True)
class LoginHandler:
    _verifier: Verifier
    _clock: Clock
    _user_repository: UserRepository
    _session_repository: SessionRepository
    _transaction_manager: TransactionManager
    _id_generator: IdGenerator
    _identity_provider: IdentityProvider

    async def handle(self, request: LoginRequest) -> Session:
        user = await self._user_repository.get_by_email(request.email)

        if not user:
            raise NotFoundError("User not found")

        if not self._verifier.verify_password(request.password, user.password_hash):
            raise AccessError()

        session = Session(
            id=self._id_generator.generate_session_id(),
            user_id=user.id,
            expires_at=self._clock.in_time(timedelta(days=30)),
        )
        self._session_repository.add(session)
        await self._transaction_manager.commit()
        return session
