from dataclasses import dataclass
from typing import List

from .types import Badge, Category


@dataclass(frozen=True)
class Bot:
    id: int
    name: str
    slug: str
    description: str
    avatar: str
    library: str
    prefix: str
    owner: List["User"]
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
    status: int = 200


@dataclass(frozen=True)
class User:
    id: int
    username: str
    descriminator: str
    avatar: str
    bots: List["Bot"]
    badges: List[Badge]
    status: int = 200


@dataclass(frozen=True)
class Vote:
    voted: bool
    status: int = 200
