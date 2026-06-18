from dishka import Provider, Scope, provide_all

from dima_tech.application.factories.user import UserFactory
from dima_tech.application.handlers.account.me import MeAccountHandler
from dima_tech.application.handlers.auth.login import LoginHandler
from dima_tech.application.handlers.auth.me import MeHandler
from dima_tech.application.handlers.payment.me import MePaymentHandler
from dima_tech.application.handlers.payment.process import PaymentProcessHandler
from dima_tech.application.handlers.user.create_user import CreateUserHandler
from dima_tech.application.handlers.user.delete_user import DeleteUserHandler
from dima_tech.application.handlers.user.get_all import GetAllUsersHandler
from dima_tech.application.handlers.user.update_user import UpdateUserHandler


class ApplicationProvider(Provider):
    scope = Scope.REQUEST

    fabrics = provide_all(UserFactory)

    handlers = provide_all(
        CreateUserHandler,
        LoginHandler,
        MeHandler,
        DeleteUserHandler,
        MeAccountHandler,
        MePaymentHandler,
        UpdateUserHandler,
        GetAllUsersHandler,
        PaymentProcessHandler,
    )
