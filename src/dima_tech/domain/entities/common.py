from dataclasses import dataclass


@dataclass
class IdEntity[T]:
    id: T
