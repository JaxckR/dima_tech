__all__ = (
    "get_async_container",
    "get_config",
)

from typing import Final

from dishka import AsyncContainer, make_async_container, Provider
from dishka.integrations.fastapi import FastapiProvider

from dima_tech.bootstrap.config import get_config, PostgresConfig, Config
from dima_tech.bootstrap.ioc.application import ApplicationProvider
from dima_tech.bootstrap.ioc.context import ContextProvider
from dima_tech.bootstrap.ioc.database import DatabaseProvider
from dima_tech.bootstrap.ioc.infrastructure import InfrastructureProvider

PROVIDERS: Final[list[Provider]] = [
    ContextProvider(),
    ApplicationProvider(),
    DatabaseProvider(),
    InfrastructureProvider(),
    FastapiProvider(),
]


def get_async_container(config: Config) -> AsyncContainer:
    return make_async_container(
        *PROVIDERS, context={PostgresConfig: config.database, Config: config}
    )
