from sqlalchemy import select

from dima_tech.application.ports.repositories import PaymentRepository
from dima_tech.domain.entities.payment import Payment
from dima_tech.domain.entities.user import UserId
from dima_tech.infrastructure.persistence.adapters.common import SQLAMixin


class PaymentRepositoryImpl(SQLAMixin, PaymentRepository):
    def add(self, instance: Payment) -> None:
        self._session.add(instance)

    async def get_by_user_id(self, user_id: UserId) -> list[Payment]:
        query = await self._session.execute(
            select(Payment).where(Payment.user_id == user_id)
        )
        return list(query.scalars().all())
