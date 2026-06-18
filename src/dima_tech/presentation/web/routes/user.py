from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter
from starlette import status

from dima_tech.application.dto import UserWithAccountsDTO
from dima_tech.application.handlers.user.create_user import (
    CreateUserRequest,
    CreateUserHandler,
)
from dima_tech.application.handlers.user.delete_user import DeleteUserHandler
from dima_tech.application.handlers.user.get_all import GetAllUsersHandler
from dima_tech.application.handlers.user.update_user import (
    UpdateUserRequest,
    UpdateUserHandler,
)
from dima_tech.domain.entities.user import UserId

user_router = APIRouter(prefix="/users", tags=["user"], route_class=DishkaRoute)


@user_router.get("/")
async def get_all(handler: FromDishka[GetAllUsersHandler]) -> list[UserWithAccountsDTO]:
    return await handler.handle()


@user_router.post("/", status_code=status.HTTP_201_CREATED)
async def create(
    request: CreateUserRequest, handler: FromDishka[CreateUserHandler]
) -> None:
    await handler.handle(request)


@user_router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(user_id: UserId, handler: FromDishka[DeleteUserHandler]) -> None:
    await handler.handle(user_id)


@user_router.patch("/{user_id}", status_code=status.HTTP_200_OK)
async def update(
    user_id: UserId, request: UpdateUserRequest, handler: FromDishka[UpdateUserHandler]
) -> None:
    await handler.handle(user_id, request)
