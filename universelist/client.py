from typing import Optional

from aiohttp import ClientSession

from .http import Router
from .models import Bot, User, Vote


class UniverseListClient(Router):
    def __init__(
        self, token: Optional[str] = None, session: Optional[ClientSession] = None
    ):
        super().__init__(token, session)

    async def bot(self, id: int) -> Bot:
        return Bot(await self.get_bots(id))

    async def user(self, id: int) -> User:
        return User(await self.get_users(id))

    async def is_voted_bot(self, bot_id: int, user_id: int) -> bool:
        return Vote(await self.get_is_voted_bot(bot_id, user_id))

    async def update_stat(self, id: int, count: int) -> bool:
        return await self.post_bot_stat(id, count)
