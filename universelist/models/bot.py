from dataclasses import dataclass
from typing import List
from ..types import Category, Badge
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