from abc import abstractmethod
from typing import Protocol

from dima_tech.domain.entities.session import SessionId


class IdGenerator(Protocol):
    @abstractmethod
    def generate_session_id(self) -> SessionId: ...
