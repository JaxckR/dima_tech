from dataclasses import dataclass
from datetime import datetime

from dima_tech.domain.entities.account import Account
from dima_tech.domain.entities.user import User, UserId


@dataclass(slots=True, frozen=True)
class UserDTO:
    id: UserId
    email: str
    full_name: str
    role: str
    created_at: datetime
    updated_at: datetime | None

    @staticmethod
    def from_entity(entity: User) -> UserDTO:
        return UserDTO(
            id=entity.id,
            email=entity.email,
            full_name=str(entity.full_name),
            role=entity.role.name,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )


@dataclass(slots=True, frozen=True)
class UserWithAccountsDTO:
    id: UserId
    email: str
    full_name: str
    role: str
    accounts: list[Account]
    created_at: datetime
    updated_at: datetime | None
