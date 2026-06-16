from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import NewType
from uuid import UUID

from dima_tech.domain.entities.account import AccountId
from dima_tech.domain.entities.common import IdEntity
from dima_tech.domain.entities.user import UserId

PaymentId = NewType("PaymentId", int)
TransactionId = NewType("TransactionId", UUID)


@dataclass
class Payment(IdEntity[PaymentId]):
    transaction_id: TransactionId
    account_id: AccountId
    user_id: UserId
    amount: Decimal
    created_at: datetime
    updated_at: datetime | None
