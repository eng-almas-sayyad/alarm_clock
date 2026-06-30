from dataclasses import dataclass

@dataclass
class Alarm:
    id: int
    time: str
    enabled: bool = True