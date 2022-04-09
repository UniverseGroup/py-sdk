from dataclasses import dataclass
from typing import List

from ..types import Badge
from .bot import Bot


@dataclass(frozen=True)
class User:
    id: int
    username: str
    descriminator: int
    avatar: str
    bots: List[Bot] = []
    badges: List[Badge] = []

    def __init__(self, data: dict) -> None:
        super().__init__(
            id=data.get("id"),
            username=data.get("username"),
            descriminator=data.get("descriminator"),
            avatar=data.get("avatar"),
            bots=data.get("bots"),
            badges=data.get("badges"),
        )
