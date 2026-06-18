from dishka import Provider, from_context, Scope

from dima_tech.bootstrap.config import PostgresConfig, Config


class ContextProvider(Provider):
    scope = Scope.APP

    database_config = from_context(PostgresConfig)
    config = from_context(Config)
