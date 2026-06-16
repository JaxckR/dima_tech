import sqlalchemy as sa

from dima_tech.domain.entities.account import Account
from .common import mapper_registry

accounts_table = sa.Table(
    "accounts",
    mapper_registry.metadata,
    sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True),
    sa.Column(
        "user_id",
        sa.BigInteger,
        sa.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    ),
    sa.Column(
        "balance", sa.Numeric(precision=18, scale=2), nullable=False, server_default="0"
    ),
    sa.Column(
        "created_at",
        sa.DateTime(timezone=True),
        server_default=sa.func.now(),
        nullable=False,
    ),
    sa.Column("updated_at", sa.DateTime(timezone=True), server_onupdate=sa.func.now()),
)


def _map_accounts_table() -> None:
    _ = mapper_registry.map_imperatively(
        Account,
        accounts_table,
        properties={
            "id": accounts_table.c.id,
            "user_id": accounts_table.c.user_id,
            "balance": accounts_table.c.balance,
            "created_at": accounts_table.c.created_at,
            "updated_at": accounts_table.c.updated_at,
        },
        column_prefix="_",
    )
