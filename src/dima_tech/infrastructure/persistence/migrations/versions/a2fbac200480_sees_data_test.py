"""Sees data test

Revision ID: a2fbac200480
Revises: 1918f83f6afa
Create Date: 2026-06-18 20:41:07.636703

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a2fbac200480'
down_revision: Union[str, Sequence[str], None] = '1918f83f6afa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# Test user: user@example.com / user12345
TEST_USER_PASSWORD_HASH = "$2b$12$Y2KAwY6Z9T/l4ThZEbSHvOlQk5qp6RfDLY4KmPN0uzYakF0379rmi"

# Test admin: admin@example.com / admin12345
TEST_ADMIN_PASSWORD_HASH = "$2b$12$FEgq/5aGDvm2J97ej8xcTeXEPTtxh3hQUj8lMQTSAD06HYFLb5nTy"


def upgrade() -> None:
    """Upgrade schema."""
    users_table = sa.table(
        "users",
        sa.column("id", sa.BigInteger),
        sa.column("email", sa.String),
        sa.column("password_hash", sa.String),
        sa.column("first_name", sa.String),
        sa.column("last_name", sa.String),
        sa.column("patronymic", sa.String),
        sa.column("role", sa.Enum("USER", "ADMIN", name="role")),
    )

    op.bulk_insert(
        users_table,
        [
            {
                "id": 1,
                "email": "user@example.com",
                "password_hash": TEST_USER_PASSWORD_HASH,
                "first_name": "Test",
                "last_name": "User",
                "patronymic": None,
                "role": "USER",
            },
            {
                "id": 2,
                "email": "admin@example.com",
                "password_hash": TEST_ADMIN_PASSWORD_HASH,
                "first_name": "Test",
                "last_name": "Admin",
                "patronymic": None,
                "role": "ADMIN",
            },
        ],
    )

    accounts_table = sa.table(
        "accounts",
        sa.column("id", sa.BigInteger),
        sa.column("user_id", sa.BigInteger),
        sa.column("balance", sa.Numeric),
    )

    op.bulk_insert(
        accounts_table,
        [
            {"id": 1, "user_id": 1, "balance": 0},
        ],
    )

    # Sync sequences after explicit id insertion, so future autoincrement
    # inserts don't collide with the seeded rows.
    op.execute(
        "SELECT setval('users_id_seq', (SELECT MAX(id) FROM users))"
    )
    op.execute(
        "SELECT setval('accounts_id_seq', (SELECT MAX(id) FROM accounts))"
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("DELETE FROM accounts WHERE id = 1")
    op.execute("DELETE FROM users WHERE id IN (1, 2)")
