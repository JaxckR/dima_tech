from datetime import datetime, timezone

from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter
from starlette import status
from starlette.responses import Response

from dima_tech.application.dto import UserDTO
from dima_tech.application.handlers.auth.login import LoginRequest, LoginHandler
from dima_tech.application.handlers.auth.me import MeHandler

auth_router = APIRouter(prefix="/auth", tags=["auth"], route_class=DishkaRoute)


@auth_router.get("/me", status_code=status.HTTP_200_OK)
async def me(handler: FromDishka[MeHandler]) -> UserDTO:
    return await handler.handle()


@auth_router.post("/login", status_code=status.HTTP_200_OK)
async def login(
    request: LoginRequest, handler: FromDishka[LoginHandler], response: Response
) -> None:
    session = await handler.handle(request)
    response.set_cookie(
        key="session_id",
        value=session.id,
        httponly=True,
        secure=True,
        samesite="strict",
        max_age=int((session.expires_at - datetime.now(timezone.utc)).total_seconds()),
    )
