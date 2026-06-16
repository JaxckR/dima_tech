from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import NewType

from dima_tech.domain.entities.common import IdEntity
from dima_tech.domain.entities.user import UserId

AccountId = NewType("AccountId", int)


@dataclass
class Account(IdEntity[AccountId]):
    user_id: UserId
    balance: Decimal
    created_at: datetime
    updated_at: datetime | None
