from datetime import datetime, timezone, timedelta

from dima_tech.application.ports import Clock


class ClockImpl(Clock):
    def in_time(self, delta: timedelta) -> datetime:
        return self.now() + delta

    def now(self) -> datetime:
        return datetime.now(timezone.utc)
