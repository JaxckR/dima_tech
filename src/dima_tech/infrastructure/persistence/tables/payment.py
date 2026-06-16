import sqlalchemy as sa

from dima_tech.domain.entities.payment import Payment
from .common import mapper_registry

payments_table = sa.Table(
    "payments",
    mapper_registry.metadata,
    sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True),
    sa.Column("transaction_id", sa.UUID(as_uuid=True), unique=True, nullable=False),
    sa.Column(
        "account_id",
        sa.BigInteger,
        sa.ForeignKey("accounts.id", ondelete="RESTRICT"),
        nullable=False,
    ),
    sa.Column(
        "user_id",
        sa.BigInteger,
        sa.ForeignKey("users.id", ondelete="RESTRICT"),
        nullable=False,
    ),
    sa.Column(
        "amount", sa.Numeric(precision=18, scale=2), nullable=False, server_default="0"
    ),
    sa.Column(
        "created_at",
        sa.DateTime(timezone=True),
        server_default=sa.func.now(),
        nullable=False,
    ),
    sa.Column("updated_at", sa.DateTime(timezone=True), server_onupdate=sa.func.now()),
)


def _map_payments_table() -> None:
    _ = mapper_registry.map_imperatively(
        Payment,
        payments_table,
        properties={
            "id": payments_table.c.id,
            "transaction_id": payments_table.c.transaction_id,
            "account_id": payments_table.c.account_id,
            "user_id": payments_table.c.user_id,
            "amount": payments_table.c.amount,
            "created_at": payments_table.c.created_at,
            "updated_at": payments_table.c.updated_at,
        },
        column_prefix="_",
    )
