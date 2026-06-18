from dataclasses import dataclass
from os import environ


@dataclass(frozen=True, slots=True)
class PostgresConfig:
    user: str
    password: str
    host: str
    port: int
    database: str

    @property
    def url(self) -> str:
        return f"postgresql+psycopg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


@dataclass(frozen=True, slots=True)
class Config:
    database: PostgresConfig
    secret_key: str


def get_config() -> Config:
    return Config(
        database=PostgresConfig(
            user=environ["POSTGRES_USER"],
            password=environ["POSTGRES_PASSWORD"],
            host=environ["POSTGRES_HOST"],
            port=int(environ["POSTGRES_PORT"]),
            database=environ["POSTGRES_DB"],
        ),
        secret_key=environ["SECRET_KEY"],
    )
