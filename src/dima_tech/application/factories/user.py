import re
from dataclasses import dataclass
from typing import cast, Final, ClassVar

from dima_tech.application.exceptions import ApplicationError
from dima_tech.application.ports import Clock, Hasher, TransactionManager
from dima_tech.domain.entities.user import User, Role, FullName


@dataclass(slots=True)
class UserFactory:
    _transaction_manager: TransactionManager
    _hasher: Hasher
    _clock: Clock

    MIN_PASSWORD_LENGTH: ClassVar[Final[int]] = 8
    EMAIL_REGEX: ClassVar[Final[re.Pattern[str]]] = re.compile(
        r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    )

    async def create(
        self,
        email: str,
        password: str,
        first_name: str,
        last_name: str,
        patronymic: str | None = None,
        role: Role = Role.USER,
    ) -> User:
        if not self.EMAIL_REGEX.match(email):
            raise ApplicationError("Invalid email")

        if len(password) < self.MIN_PASSWORD_LENGTH:
            raise ApplicationError("Password too short")

        password_hash = self._hasher.hash_password(password)
        user = User(
            id=cast(int, cast(object, None)),
            email=email,
            password_hash=password_hash,
            full_name=FullName(
                first_name=first_name, last_name=last_name, patronymic=patronymic
            ),
            role=role,
            created_at=self._clock.now(),
            updated_at=None,
        )
        await self._transaction_manager.flush()
        return user
