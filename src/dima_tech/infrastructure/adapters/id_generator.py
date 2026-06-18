from secrets import token_urlsafe

from dima_tech.application.ports import IdGenerator
from dima_tech.domain.entities.session import SessionId


class IdGeneratorImpl(IdGenerator):
    def generate_session_id(self) -> SessionId:
        return SessionId(token_urlsafe(32))
