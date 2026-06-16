from contextlib import asynccontextmanager
from typing import AsyncIterator

import uvicorn
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from dima_tech.bootstrap.config import get_config
from dima_tech.bootstrap.ioc import get_async_container
from dima_tech.bootstrap.logging import setup_logging
from dima_tech.infrastructure.persistence.tables import setup_tables
from dima_tech.presentation.web.exception_handler import setup_exceptions
from dima_tech.presentation.web.routes import setup_routes


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    yield
    await app.state.dishka_container.close()


def create_app() -> FastAPI:
    app = FastAPI(
        title="Dima_tech",
        description="Тестовое задание для компании DimaTech",
        version="1.0.0",
        lifespan=lifespan,
    )
    config = get_config()
    setup_logging()
    setup_dishka(get_async_container(config), app)
    setup_tables()
    setup_exceptions(app)
    setup_routes(app)
    return app


if __name__ == "__main__":
    uvicorn.run(create_app(), host="0.0.0.0", port=8000)
