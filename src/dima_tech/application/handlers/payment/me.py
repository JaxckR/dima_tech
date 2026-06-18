from dataclasses import dataclass

from dima_tech.application.exceptions import AccessError
from dima_tech.application.ports import IdentityProvider
from dima_tech.application.ports.repositories import PaymentRepository
from dima_tech.domain.entities.payment import Payment


@dataclass(slots=True, frozen=True)
class MePaymentHandler:
    _identity_provider: IdentityProvider
    _payment_repository: PaymentRepository

    async def handle(self) -> list[Payment]:
        user_id = await self._identity_provider.get_user_id()

        if user_id is None:
            raise AccessError()

        return await self._payment_repository.get_by_user_id(user_id)
