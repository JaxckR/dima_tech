__all__ = (
    "mapper_registry",
    "setup_tables",
    "users_table",
    "accounts_table",
    "payments_table",
    "sessions_table",
)

from .account import _map_accounts_table, accounts_table
from .common import mapper_registry
from .payment import _map_payments_table, payments_table
from .session import _map_sessions_table, sessions_table
from .user import _map_users_table, users_table


def setup_tables() -> None:
    _map_users_table()
    _map_accounts_table()
    _map_payments_table()
    _map_sessions_table()
