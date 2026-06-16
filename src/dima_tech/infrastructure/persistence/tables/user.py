import sqlalchemy as sa
from sqlalchemy.orm import composite

from dima_tech.domain.entities.user import Role, User, FullName
from .common import mapper_registry

users_table = sa.Table(
    "users",
    mapper_registry.metadata,
    sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True),
    sa.Column("email", sa.String(255), nullable=False, unique=True),
    sa.Column("password_hash", sa.String, nullable=False),
    sa.Column("first_name", sa.String(255), nullable=False),
    sa.Column("last_name", sa.String(255), nullable=False),
    sa.Column("patronymic", sa.String(255)),
    sa.Column("role", sa.Enum(Role), nullable=False, server_default=Role.USER.name),
    sa.Column(
        "created_at",
        sa.DateTime(timezone=True),
        server_default=sa.func.now(),
        nullable=False,
    ),
    sa.Column("updated_at", sa.DateTime(timezone=True), server_onupdate=sa.func.now()),
)


def _map_users_table() -> None:
    _ = mapper_registry.map_imperatively(
        User,
        users_table,
        properties={
            "id": users_table.c.id,
            "email": users_table.c.email,
            "password_hash": users_table.c.password_hash,
            "full_name": composite(
                FullName,
                users_table.c.first_name,
                users_table.c.last_name,
                users_table.c.patronymic,
            ),
            "role": users_table.c.role,
            "created_at": users_table.c.created_at,
            "updated_at": users_table.c.updated_at,
        },
        column_prefix="_",
    )
