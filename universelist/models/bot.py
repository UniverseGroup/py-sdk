from dataclasses import dataclass
from typing import List

from ..types import Badge, Category
from .user import User


@dataclass(frozen=True)
class Bot:
    id: int
    name: str
    slug: str
    descroption: str
    avatar: str
    library: str
    prefix: str
    owner: List[User]
    status: str
    hearts: int
    guilds: int
    category: List[Category]
    website: str
    support: str
    github: str
    banner: str
    state: str
    badges: List[Badge]
    locked: bool

    def __init__(self, data: dict) -> None:
        super().__init__(
            id=data.get("id", 0),
            name=data.get("name", ""),
            slug=data.get("slug", ""),
            descroption=data.get("descroption", ""),
            avatar=data.get("avatar", ""),
            library=data.get("library", ""),
            prefix=data.get("prefix", ""),
            owner=data.get("owner", []),
            status=data.get("status", ""),
            hearts=data.get("hearts", 0),
            guilds=data.get("guilds", 0),
            category=data.get("category", []),
            website=data.get("website", ""),
            support=data.get("support", ""),
            github=data.get("github", ""),
            banner=data.get("banner", ""),
            state=data.get("state", ""),
            badges=data.get("badges", []),
            locked=data.get("locked", False),
        )
