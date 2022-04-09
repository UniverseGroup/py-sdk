import pytest

from universelist.client import UniverseListClient
from universelist.models import Bot, User

@pytest.mark.asyncio
async def get_bot(client: UniverseListClient):
    res = client.bot(774280026958331905)
    assert res.status = 200
    assert isinstance(res.owner[0], User)
    
@pytest.mark.asyncio
async def get_bot(client: UniverseListClient):
    res = client.user(354184274347294720)
    assert res.status = 200
    assert isinstance(res.bots[0], Bot)
    