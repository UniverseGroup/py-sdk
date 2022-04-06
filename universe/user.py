from dataclass import dataclass
from typing import List
from .types import Badge
from .bot import Bot

@dataclass(frozen=True)
class User:
    id: int
    username: str
    descriminator: int
    avatar: str
    bots: List[Bot] = []
    badges: List[Badge] = []