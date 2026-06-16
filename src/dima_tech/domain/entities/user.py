from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from typing import NewType

from dima_tech.domain.entities.common import IdEntity

UserId = NewType("UserId", int)


class Role(StrEnum):
    ADMIN = "admin"
    USER = "user"


@dataclass(slots=True, frozen=True)
class FullName:
    first_name: str
    last_name: str
    patronymic: str | None = None

    def __str__(self) -> str:
        parts = [self.last_name, self.first_name]

        if self.patronymic is not None:
            parts.append(self.patronymic)

        return " ".join(parts)


@dataclass
class User(IdEntity[UserId]):
    email: str
    password_hash: str
    full_name: FullName
    role: Role
    created_at: datetime
    updated_at: datetime | None
