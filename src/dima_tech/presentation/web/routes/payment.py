from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter
from starlette import status

from dima_tech.application.handlers.payment.me import MePaymentHandler
from dima_tech.domain.entities.payment import Payment

payment_router = APIRouter(
    prefix="/payments", tags=["payment"], route_class=DishkaRoute
)


@payment_router.get("/me", status_code=status.HTTP_200_OK)
async def get_user_payments(handler: FromDishka[MePaymentHandler]) -> list[Payment]:
    return await handler.handle()
