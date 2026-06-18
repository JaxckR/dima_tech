from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter
from starlette import status

from dima_tech.application.handlers.account.me import MeAccountHandler
from dima_tech.domain.entities.account import Account

account_router = APIRouter(
    prefix="/accounts", tags=["account"], route_class=DishkaRoute
)


@account_router.get("/me", status_code=status.HTTP_200_OK)
async def get_user_accounts(handler: FromDishka[MeAccountHandler]) -> list[Account]:
    return await handler.handle()
