from dataclasses import dataclass
from datetime import datetime
from typing import NewType

from dima_tech.domain.entities.common import IdEntity
from dima_tech.domain.entities.user import UserId

SessionId = NewType("SessionId", str)


@dataclass
class Session(IdEntity[SessionId]):
    user_id: UserId
    expires_at: datetime
