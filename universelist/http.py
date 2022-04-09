import asyncio
from datetime import datetime
from typing import Any, Literal, Optional

from aiohttp import ClientSession

from . import errors

Status = {
    400: errors.HTTPException,
    401: errors.Unauthorized,
    403: errors.Forbidden,
    404: errors.NotFound,
}


class Router:
    def __init__(
        self, token: Optional[str] = None, session: Optional[ClientSession] = None
    ) -> None:
        self.BASE = "https://universelist.kr/api/"

        self.token = token
        self.session: Optional[ClientSession] = None
        self._session = session is None

    async def request(
        self,
        method: Literal["GET", "POST"],
        endpoint: str,
        authorize: Optional[bool] = False,
        **kwargs: Any,
    ) -> dict:
        headers = {"Content-Type": "application/json; charset=utf-8"}
        if authorize is True:
            if not self.token:
                raise errors.TokenNotDetected("API 토큰이 제공되지 않았습니다.")
            headers["Authorization"] = self.token

        kwargs["headers"] = headers

        for _ in range(3):
            async with self.session.request(
                method, self.BASE + endpoint, **kwargs
            ) as res:
                data = res.json()

                if 200 <= res.status < 300:
                    return data

                elif res.status == 429:
                    if res.headers.get("X-RateLimit-Remaining"):
                        if res.headers["X-RateLimit-Remaining"] == 0:
                            reset = datetime.fromtimestamp(
                                int(res.headers.get("X-Ratelimit-Reset", 1))
                            )
                            sleep_seconds = reset - datetime.now()
                            await asyncio.sleep(sleep_seconds.total_seconds())
                    else:
                        await asyncio.sleep(60)

                    continue
                elif res.status >= 500:
                    raise errors.ServerException(res, data)

                else:
                    if Status.get(res.status):
                        raise Status[res.status](res, data)

        raise errors.HTTPException(res, data)

    async def close(
        self,
    ) -> None:
        if self._session:
            await self.session.close()

    async def get_bots(self, id: int) -> dict:
        return await self.request("GET", f"bots/{id}")

    async def get_users(self, id: int) -> dict:
        return await self.request("GET", f"users/{id}")

    async def get_is_voted_bot(self, bot_id: int, user_id: int) -> dict:
        return await self.request(
            "GET", f"bots/{bot_id}/vote", params={"userid": user_id}
        )

    async def post_bot_guild_count(self, id: int, count: int) -> dict:
        return await self.request("POST", f"bots/{id}/stat", data={"servers": count})
