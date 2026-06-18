from sqlalchemy import select, delete

from dima_tech.application.ports.repositories import UserRepository
from dima_tech.domain.entities.user import User, UserId
from dima_tech.infrastructure.persistence.adapters.common import SQLAMixin


class UserRepositoryImpl(SQLAMixin, UserRepository):
    async def delete(self, id_: UserId) -> None:
        await self._session.execute(delete(User).where(User.id == id_))

    async def get_by_email(self, email: str) -> User | None:
        query = await self._session.execute(select(User).where(User.email == email))
        return query.scalar_one_or_none()

    async def get(self, id_: UserId) -> User | None:
        query = await self._session.execute(select(User).where(User.id == id_))
        return query.scalar_one_or_none()

    def add(self, instance: User) -> None:
        self._session.add(instance)
