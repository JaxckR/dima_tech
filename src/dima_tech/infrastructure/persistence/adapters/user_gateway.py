from collections import defaultdict

from sqlalchemy import select, RowMapping

from dima_tech.application.dto import UserWithAccountsDTO
from dima_tech.application.ports.gateways import UserGateway
from dima_tech.domain.entities.account import Account
from dima_tech.domain.entities.user import User, UserId
from dima_tech.infrastructure.persistence.adapters.common import SQLAMixin


class UserGatewayImpl(SQLAMixin, UserGateway):
    def _map_to_dto(self, row: RowMapping) -> UserWithAccountsDTO:
        user: User = row["User"]
        account: Account = row["Account"]
        print(row)
        return UserWithAccountsDTO(
            id=user.id,
            email=user,
            full_name=user,
            role=user,
            accounts=account,
            created_at=user,
            updated_at=user,
        )

    async def get_all_with_accounts(self) -> list[UserWithAccountsDTO]:
        query = await self._session.execute(
            select(User, Account)
            .outerjoin(Account, User.id == Account.user_id)
            .order_by(User.id)
        )

        accounts_by_user: dict[UserId, list[Account]] = defaultdict(list)
        users_by_id: dict[UserId, User] = {}

        for user, account in query.all():
            users_by_id[user.id] = user
            if account is not None:
                accounts_by_user[user.id].append(account)

        return [
            UserWithAccountsDTO(
                id=user.id,
                email=user.email,
                full_name=str(user.full_name),
                role=user.role.name,
                accounts=accounts_by_user[user.id],
                created_at=user.created_at,
                updated_at=user.updated_at,
            )
            for user in users_by_id.values()
        ]
