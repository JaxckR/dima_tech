from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter
from starlette import status

index_router = APIRouter(tags=["index"], route_class=DishkaRoute)


@index_router.get("/healthcheck", status_code=status.HTTP_200_OK)
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}
