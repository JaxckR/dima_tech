from dataclasses import dataclass
from decimal import Decimal
from typing import cast

from dima_tech.application.exceptions import ApplicationError
from dima_tech.application.ports import Verifier, Clock, TransactionManager
from dima_tech.application.ports.repositories import (
    AccountRepository,
    PaymentRepository,
)
from dima_tech.domain.entities.account import AccountId, Account
from dima_tech.domain.entities.payment import TransactionId, Payment
from dima_tech.domain.entities.user import UserId


@dataclass(slots=True, frozen=True)
class PaymentProcessRequest:
    transaction_id: TransactionId
    account_id: AccountId
    user_id: UserId
    amount: str
    signature: str


@dataclass(slots=True, frozen=True)
class PaymentProcessHandler:
    _verifier: Verifier
    _clock: Clock
    _account_repository: AccountRepository
    _payment_repository: PaymentRepository
    _transaction_manager: TransactionManager

    async def handle(self, request: PaymentProcessRequest) -> None:
        if not self._verifier.verify_transaction(
            transaction_id=request.transaction_id,
            account_id=request.account_id,
            user_id=request.user_id,
            amount=request.amount,
            signature=request.signature,
        ):
            raise ApplicationError()

        account = await self._account_repository.get(request.account_id)

        if not account:
            account = Account(
                id=request.account_id,
                user_id=request.user_id,
                balance=Decimal(0),
                created_at=self._clock.now(),
                updated_at=None,
            )
            self._account_repository.add(account)

        payment = Payment(
            id=cast(int, cast(object, None)),
            transaction_id=request.transaction_id,
            account_id=request.account_id,
            user_id=request.user_id,
            amount=Decimal(request.amount),
            created_at=self._clock.now(),
            updated_at=None,
        )
        self._payment_repository.add(payment)

        await self._account_repository.increase_balance(
            account.id, Decimal(request.amount)
        )
        await self._transaction_manager.commit()
