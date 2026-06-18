from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter
from starlette import status

from dima_tech.application.handlers.payment.process import (
    PaymentProcessHandler,
    PaymentProcessRequest,
)

webhook_router = APIRouter(
    prefix="/webhooks", tags=["webhooks"], route_class=DishkaRoute
)


@webhook_router.post("/payment", status_code=status.HTTP_200_OK)
async def payment_hook(
    request: PaymentProcessRequest, handler: FromDishka[PaymentProcessHandler]
) -> None:
    await handler.handle(request)
