from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from dima_tech.application.exceptions import AlreadyExists
from dima_tech.application.ports.repositories import PaymentRepository
from dima_tech.domain.entities.payment import Payment
from dima_tech.domain.entities.user import UserId
from dima_tech.infrastructure.persistence.adapters.common import SQLAMixin


class PaymentRepositoryImpl(SQLAMixin, PaymentRepository):
    async def add(self, instance: Payment) -> None:
        self._session.add(instance)
        try:
            await self._session.flush()
        except IntegrityError as e:
            await self.handle_exception(e)

    async def get_by_user_id(self, user_id: UserId) -> list[Payment]:
        query = await self._session.execute(
            select(Payment).where(Payment.user_id == user_id)
        )
        return list(query.scalars().all())

    async def handle_exception(self, exc: IntegrityError) -> None:
        e = str(exc)
        if "uq_payments_transaction_id" in e:
            raise AlreadyExists("Transaction already exists")
        await self._session.rollback()
