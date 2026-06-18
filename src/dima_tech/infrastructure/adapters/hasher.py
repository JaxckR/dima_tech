import bcrypt

from dima_tech.application.ports import Hasher


class HasherImpl(Hasher):
    def hash_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt).decode()
