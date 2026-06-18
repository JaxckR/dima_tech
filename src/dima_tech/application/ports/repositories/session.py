from abc import abstractmethod
from typing import Protocol

from dima_tech.domain.entities.session import SessionId, Session


class SessionRepository(Protocol):
    @abstractmethod
    def add(self, instance: Session) -> None: ...

    @abstractmethod
    async def get(self, id_: SessionId) -> Session | None: ...
