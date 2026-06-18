from dishka import Provider, Scope, provide_all, WithParents

from dima_tech.infrastructure.adapters.clock import ClockImpl
from dima_tech.infrastructure.adapters.hasher import HasherImpl
from dima_tech.infrastructure.adapters.id_generator import IdGeneratorImpl
from dima_tech.infrastructure.adapters.idp import IdentityProviderImpl
from dima_tech.infrastructure.adapters.verifier import VerifierImpl
from dima_tech.infrastructure.persistence.adapters.account_repository import (
    AccountRepositoryImpl,
)
from dima_tech.infrastructure.persistence.adapters.payment_repository import (
    PaymentRepositoryImpl,
)
from dima_tech.infrastructure.persistence.adapters.session_repository import (
    SessionRepositoryImpl,
)
from dima_tech.infrastructure.persistence.adapters.user_gateway import UserGatewayImpl
from dima_tech.infrastructure.persistence.adapters.user_repository import (
    UserRepositoryImpl,
)


class InfrastructureProvider(Provider):
    scope = Scope.REQUEST

    adapters = provide_all(
        WithParents[ClockImpl],
        WithParents[HasherImpl],
        WithParents[VerifierImpl],
        WithParents[IdentityProviderImpl],
        WithParents[IdGeneratorImpl],
    )

    repositories = provide_all(
        WithParents[UserRepositoryImpl],
        WithParents[SessionRepositoryImpl],
        WithParents[AccountRepositoryImpl],
        WithParents[PaymentRepositoryImpl],
    )

    gateways = provide_all(WithParents[UserGatewayImpl])
