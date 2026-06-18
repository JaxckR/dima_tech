__all__ = ("setup_routes",)

from typing import Final

from fastapi import FastAPI, APIRouter

from dima_tech.presentation.web.routes.account import account_router
from dima_tech.presentation.web.routes.auth import auth_router
from dima_tech.presentation.web.routes.index import index_router
from dima_tech.presentation.web.routes.payment import payment_router
from dima_tech.presentation.web.routes.user import user_router
from dima_tech.presentation.web.routes.webhooks import webhook_router

ROUTERS: Final[list[APIRouter]] = [
    index_router,
    auth_router,
    account_router,
    payment_router,
    user_router,
    webhook_router,
]


def setup_routes(app: FastAPI) -> None:
    for router in ROUTERS:
        app.include_router(router)
