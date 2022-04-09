import asyncio
from optparse import Option
from typing import Optional, Union

from aiohttp import ClientSession

from .client import UniverseListClient
from .errors import ClientException

try:
    from discord import Client
except ImportError:
    print("Discord.py is not installed.")
    pass


class DiscordUniverseList(UniverseListClient):
    def __init__(self, client: Union[Client, None], token: str):
        self.client = client
        self.token = token
        self.session = Optional[ClientSession] = None
        super().__init__(token)

        self.loop = self.client.loop
        self.loop.create_task(self.update_bot_stat())

    async def update_bot_stat(self):
        if self.client is None:
            raise ClientException("Client is not defined.")

        while self.loop.is_running:
            if self.client.is_ready():
                await self.update_stat(self.client.user.id, self.client.guilds)
            await asyncio.sleep(3600)
