from abc import abstractmethod
from datetime import datetime, timedelta
from typing import Protocol


class Clock(Protocol):
    @abstractmethod
    def now(self) -> datetime: ...

    @abstractmethod
    def in_time(self, delta: timedelta) -> datetime: ...
