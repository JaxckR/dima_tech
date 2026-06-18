from sqlalchemy import select

from dima_tech.application.ports.repositories import SessionRepository
from dima_tech.domain.entities.session import SessionId, Session
from dima_tech.infrastructure.persistence.adapters.common import SQLAMixin


class SessionRepositoryImpl(SQLAMixin, SessionRepository):
    def add(self, instance: Session) -> None:
        self._session.add(instance)

    async def get(self, id_: SessionId) -> Session | None:
        query = await self._session.execute(select(Session).where(Session.id == id_))
        return query.scalar_one_or_none()
