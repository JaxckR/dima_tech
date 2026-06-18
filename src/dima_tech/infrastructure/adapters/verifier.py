import hashlib

import bcrypt

from dima_tech.application.ports import Verifier
from dima_tech.bootstrap.config import Config
from dima_tech.domain.entities.account import AccountId
from dima_tech.domain.entities.payment import TransactionId
from dima_tech.domain.entities.user import UserId


class VerifierImpl(Verifier):
    def __init__(self, config: Config) -> None:
        self._config = config

    def verify_transaction(
        self,
        transaction_id: TransactionId,
        account_id: AccountId,
        user_id: UserId,
        amount: str,
        signature: str,
    ) -> bool:
        raw = f"{account_id}{amount}{transaction_id}{user_id}{self._config.secret_key}"
        expected = hashlib.sha256(raw.encode()).hexdigest()
        return expected == signature

    def verify_password(self, password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(password.encode(), hashed_password.encode())
