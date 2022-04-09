from typing import Optional

from aiohttp import ClientSession

from .http import Router
from .models import Bot, User, Vote
from .types import Category


class UniverseListClient(Router):
    def __init__(
        self, token: Optional[str] = None, session: Optional[ClientSession] = None
    ):
        super().__init__(token, session)

    async def bot(self, id: int) -> Bot:
        data = await self.get_bots(id)
        return Bot(
            id=data.get("botid", 0),
            name=data.get("botname", ""),
            slug=data.get("slug", ""),
            description=data.get("botdescription", ""),
            avatar=data.get("botavatar", ""),
            library=data.get("library", ""),
            prefix=data.get("prefix", ""),
            owner=list(
                map(
                    lambda user: User(
                        id=user.get("id", 0),
                        username=user.get("username", ""),
                        descriminator=user.get("discriminator", ""),
                        avatar=user.get("useravatar", ""),
                    ),
                    data.get("owner", []),
                )
            ),
            status=data.get("status", ""),
            hearts=data.get("hearts", 0),
            guilds=data.get("guilds", 0),
            category=list(
                map(
                    lambda category: Category(
                        category.get("label", ""),
                    ),
                    data.get("category", []),
                )
            ),
            website=data.get("website", ""),
            support=data.get("support", ""),
            github=data.get("github", ""),
            banner=data.get("banner", ""),
            state=data.get("state", ""),
            badges=data.get("badges", []),
            locked=data.get("locked", False),
        )

    async def user(self, id: int) -> User:
        data = await self.get_users(id)
        return User(
            id=data.get("userid", 0),
            username=data.get("username", ""),
            descriminator=data.get("discriminator", ""),
            avatar=data.get("useravatar", ""),
            bots=list(
                map(
                    lambda bot: Bot(
                        id=bot.get("botid", 0),
                        name=bot.get("botname", ""),
                        slug=bot.get("slug", ""),
                        description=bot.get("botdescription", ""),
                        avatar=bot.get("botavatar", ""),
                        library=bot.get("library", ""),
                        prefix=bot.get("prefix", ""),
                        owner=list(
                            map(
                                lambda user: User(
                                    id=user.get("id", 0),
                                    username=user.get("username", ""),
                                    descriminator=user.get("discriminator", ""),
                                    avatar=user.get("useravatar", ""),
                                ),
                                bot.get("owner", []),
                            )
                        ),
                        status=bot.get("status", ""),
                        hearts=bot.get("hearts", 0),
                        guilds=bot.get("guilds", 0),
                        category=list(
                            map(
                                lambda category: Category(
                                    category.get("label", ""),
                                ),
                                bot.get("category", []),
                            )
                        ),
                        website=bot.get("website", ""),
                        support=bot.get("support", ""),
                        github=bot.get("github", ""),
                        banner=bot.get("banner", ""),
                        state=bot.get("state", ""),
                        badges=bot.get("badges", []),
                        locked=bot.get("locked", False),
                    ),
                    data.get("bots", []),
                )
            ),
            badges=data.get("badges", []),
        )

    async def is_voted_bot(self, bot_id: int, user_id: int) -> bool:
        data = await self.get_bot_vote(bot_id, user_id)
        return Vote(
            voted=True if data.get("status", 0) == 200 else False,
        )

    async def update_stat(self, id: int, count: int) -> bool:
        return await self.post_bot_stat(id, count)
