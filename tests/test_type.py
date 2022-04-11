import pytest

from universelist import types
from universelist.models import Bot, User, Vote

bot_data = {
    "botid": "774280026958331905",
    "botname": "왓치독 WatchDog",
    "botdescription": """
    # 왓치독 WatchDog
    
    ## 인증 시스템
    - 차단(밴)을 무시하기 위해 사용되는 VPN 감지
    
    ## 자동 관리 시스템
    > 보다 편리하게 서버를 관리하세요!
    
    - 앞메
        - 허용되지 않은 서버내 채널에서 보내진 초대링크 감지
    - 멘션도배
        - 여러 유저를 멘션한 메세지 감지
    - 도배
        - 메세지 일치성을 이용하여 스팸 메세지 감지
    - 링크
        - 웹사이트 링크를 감지
    - 토큰도배
        - 토큰으로 의심되는 계정을 감지
    
    ## 화이트리스트
    > 자동 관리 시스템을 무시할 채널을 설정해보세요!
    
    - 채널 및 역할
        - 채널과 역할을 자동 관리 시스템으로부터 무시
        
    ## 보안 기능
    > 서버 보안을 강화하기 위해 사용해보세요!
    
    - 보안초대링크
        - 봇이 생성하는 초대링크를 통해 뒷메 유저를 방어
    """,
    "botavatar": "https://cdn.discordapp.com/avatars/774280026958331905/07fd1cca3488831adec255920c6ae612.png",
    "owners": [
        {
            "id": "354184274347294720",
            "username": "InsanePhin",
            "discriminator": "5626",
            "avatar": "https://cdn.discordapp.com/avatars/354184274347294720/9e0bfe3888a41747de942ded24a22b6a.png%27%7D",
        }
    ],
    "approved": True,
    "banned": False,
    "bannedreason": "",
    "library": "discord.py",
    "prefix": ".",
    "trusted": False,
    "guilds": 0,
    "discordVerified": True,
    "status": "online",
    "invite": "https://discord.com/oauth2/authorize?client_id=774280026958331905&permissions=8&scope=bot%20applications.commands",
    "hearts": 2,
    "slug": "디스코드가 깨끗해지는 그날까지",
    "premium": False,
    "category": [
        {"value": "manage", "label": "관리"},
        {"value": "slash", "label": "빗금명령어"},
    ],
    "website": "",
    "support": "",
    "github": "",
    "banner": None,
    "badges": [],
    "users": 0,
    "locked": False,
}

user_data = {
    "userid": "354184274347294720",
    "badges": [],
    "bots": [
        {
            "botid": "774280026958331905",
            "botname": "\uc653\uce58\ub3c5 WatchDog",
            "botdescription": "# \uc653\uce58\ub3c5 WatchDog\n\n## \uc778\uc99d \uc2dc\uc2a4\ud15c\n- \ucc28\ub2e8(\ubc34)\uc744 \ubb34\uc2dc\ud558\uae30 \uc704\ud574 \uc0ac\uc6a9\ub418\ub294 `VPN \uac10\uc9c0`\n\n## \uc790\ub3d9 \uad00\ub9ac \uc2dc\uc2a4\ud15c\n> \ubcf4\ub2e4 \ud3b8\ub9ac\ud558\uac8c \uc11c\ubc84\ub97c \uad00\ub9ac\ud558\uc138\uc694!\n\n- \uc55e\uba54\n    - \ud5c8\uc6a9\ub418\uc9c0 \uc54a\uc740 \uc11c\ubc84\ub0b4 \ucc44\ub110\uc5d0\uc11c \ubcf4\ub0b4\uc9c4 `\ucd08\ub300\ub9c1\ud06c` \uac10\uc9c0\n\n- \uba58\uc158\ub3c4\ubc30\n    - \uc5ec\ub7ec \uc720\uc800\ub97c `\uba58\uc158\ud55c \uba54\uc138\uc9c0` \uac10\uc9c0\n\n- \ub3c4\ubc30\n    - \uba54\uc138\uc9c0 \uc77c\uce58\uc131\uc744 \uc774\uc6a9\ud558\uc5ec `\uc2a4\ud338 \uba54\uc138\uc9c0` \uac10\uc9c0\n\n- \ub9c1\ud06c\n    - \uc6f9\uc0ac\uc774\ud2b8 `\ub9c1\ud06c`\ub97c \uac10\uc9c0\n\n- \ud1a0\ud070\ub3c4\ubc30\n    - \ud1a0\ud070\uc73c\ub85c \uc758\uc2ec\ub418\ub294 `\uacc4\uc815`\uc744 \uac10\uc9c0\n\n## \ud654\uc774\ud2b8\ub9ac\uc2a4\ud2b8\n> \uc790\ub3d9 \uad00\ub9ac \uc2dc\uc2a4\ud15c\uc744 \ubb34\uc2dc\ud560 \ucc44\ub110\uc744 \uc124\uc815\ud574\ubcf4\uc138\uc694!\n\n- \ucc44\ub110 \ubc0f \uc5ed\ud560\n    - `\ucc44\ub110`\uacfc `\uc5ed\ud560`\uc744 `\uc790\ub3d9 \uad00\ub9ac \uc2dc\uc2a4\ud15c`\uc73c\ub85c\ubd80\ud130 \ubb34\uc2dc\n\n## \ubcf4\uc548 \uae30\ub2a5\n> \uc11c\ubc84 \ubcf4\uc548\uc744 \uac15\ud654\ud558\uae30 \uc704\ud574 \uc0ac\uc6a9\ud574\ubcf4\uc138\uc694!\n\n- \ubcf4\uc548\ucd08\ub300\ub9c1\ud06c\n    - \ubd07\uc774 \uc0dd\uc131\ud558\ub294 `\ucd08\ub300\ub9c1\ud06c`\ub97c \ud1b5\ud574 `\ub4b7\uba54 \uc720\uc800`\ub97c \ubc29\uc5b4",
            "botavatar": "https://cdn.discordapp.com/avatars/774280026958331905/07fd1cca3488831adec255920c6ae612.png",
            "owners": [
                {
                    "id": "354184274347294720",
                    "username": "InsanePhin",
                    "discriminator": "5626",
                    "avatar": "https://cdn.discordapp.com/avatars/354184274347294720/9e0bfe3888a41747de942ded24a22b6a.png",
                }
            ],
            "approved": True,
            "banned": False,
            "bannedreason": "",
            "library": "discord.py",
            "prefix": ".",
            "token": "",
            "trusted": False,
            "guilds": 0,
            "discordVerified": True,
            "status": "online",
            "invite": "https://discord.com/oauth2/authorize?client_id=774280026958331905&permissions=8&scope=bot%20applications.commands",
            "hearts": 0,
            "slug": "\ub514\uc2a4\ucf54\ub4dc\uac00 \uae68\ub057\ud574\uc9c0\ub294 \uadf8\ub0a0\uae4c\uc9c0",
            "premium": False,
            "category": [
                {"value": "manage", "label": "\uad00\ub9ac"},
                {"value": "slash", "label": "\ube57\uae08\uba85\ub839\uc5b4"},
            ],
            "website": "",
            "support": "",
            "github": "",
            "banner": None,
            "badges": [],
            "users": 0,
            "locked": False,
            "_id": "624b7a850a66b7dd17d63673",
        },
        {
            "botid": "851480814054539264",
            "botname": "KDDB",
            "botdescription": '# KDDB (\ud55c\uad6d \ub514\uc2a4\ucf54\ub4dc \uc0ac\uc804 \ubd07)\n"\ub514\uc2a4\ucf54\ub4dc\uc758 \ubaa8\ub4e0 \uc815\ubcf4\ub97c \uc54c\uace0 \uc2f6\uc740 \uc0ac\ub78c, \ub514\uc2a4\ucf54\ub4dc\ub97c \ucc98\uc74c \uc0ac\uc6a9\ud558\ub294 \uc0ac\ub78c\uc774 \ubaa8\ub450 \uc6d0\ud558\ub294 \uc815\ubcf4\ub97c \uc5bb\uc744 \uc218 \uc788\uc2b5\ub2c8\ub2e4"\n\n## \uae30\ub2a5\nKDD\uc5d0 \uc788\ub294 \uc815\ubcf4\ub4e4\uc744 \uc5b4\ub5a4 \uc11c\ubc84\uc5d0\uc11c\ub4e0 \uc0ac\uc6a9\ud560 \uc218 \uc788\uac8c \uc81c\uc791\ub41c \ubd07 \uc785\ub2c8\ub2e4.\n\ub204\uad6c\ub098 \uc27d\uac8c \ub514\uc2a4\ucf54\ub4dc\ub97c \uafb8\ubc00 \uc218 \uc788\uace0, \uc815\ubcf4\ub97c \uc5bb\uae30\ub97c \uc6d0\ud569\ub2c8\ub2e4.\n\n- \uc0ac\uc804\n\uae00\uc790 \uafb8\ubbf8\uae30, \uc0c9\uae54 \ubc14\uafb8\uae30, \uc11c\ubc84 \ud301, \ucc44\ud305\uce78 \uafb8\ubbf8\uae30 \ub4f1 \ub2e4\uc591\ud55c \uc815\ubcf4\ub97c \uc5bb\uc744 \uc218 \uc788\ub294 \uc0ac\uc804\uae30\ub2a5\uc785\ub2c8\ub2e4. \n\ub098\ub9cc \ubcfc \uc218\ub3c4 \uc788\uace0, \ub2e4\ub978 \uc0ac\ub78c\uacfc \uacf5\uc720\ud558\uba74\uc11c \ubcfc \uc218\ub3c4 \uc788\uc2b5\ub2c8\ub2e4.',
            "botavatar": "https://cdn.discordapp.com/avatars/851480814054539264/a014c849ae6aca777a0b155cbdb76466.png",
            "owners": [
                {
                    "id": "354184274347294720",
                    "username": "InsanePhin",
                    "discriminator": "5626",
                    "avatar": "https://cdn.discordapp.com/avatars/354184274347294720/87724268a73ae11a86b478eb44a299e2.png",
                }
            ],
            "approved": True,
            "banned": False,
            "bannedreason": "",
            "library": "discord.py",
            "prefix": "!",
            "token": "",
            "trusted": False,
            "guilds": 0,
            "discordVerified": True,
            "status": "online",
            "invite": "https://discord.com/oauth2/authorize?client_id=851480814054539264&permissions=283467902016&scope=applications.commands%20bot",
            "hearts": 0,
            "slug": "\ub514\uc2a4\ucf54\ub4dc\ub97c \uc54c\uace0 \uc2f6\ub2e4\uba74 KDDB\ub97c \uc0ac\uc6a9\ud574\ubcf4\uc138\uc694 (\ub514\uc2a4\ucf54\ub4dc\uc758 \ubaa8\ub4e0 \uc815\ubcf4\uac00 \uc788\ub294 \uc0ac\uc804\ubd07)",
            "premium": False,
            "category": [{"value": "slash", "label": "\ube57\uae08\uba85\ub839\uc5b4"}],
            "website": "",
            "support": "",
            "github": "",
            "banner": None,
            "badges": [],
            "users": 0,
            "locked": False,
            "_id": "624d7916643856725f064218",
        },
    ],
    "discriminator": "5626",
    "permissions": 0,
    "useravatar": "https://cdn.discordapp.com/avatars/354184274347294720/87724268a73ae11a86b478eb44a299e2.webp",
    "username": "InsanePhin",
}

vote_data = {"status": 200, "message": "This User have already voted for this bot"}


@pytest.fixture
def bot_data():
    return Bot(
        id=bot_data.get("botid", 0),
        name=bot_data.get("botname", ""),
        slug=bot_data.get("slug", ""),
        description=bot_data.get("botdescription", ""),
        avatar=bot_data.get("botavatar", ""),
        library=bot_data.get("library", ""),
        prefix=bot_data.get("prefix", ""),
        owner=list(
            map(
                lambda user: User(
                    id=user.get("id", 0),
                    username=user.get("username", ""),
                    descriminator=user.get("discriminator", ""),
                    avatar=user.get("useravatar", ""),
                ),
                bot_data.get("owner", []),
            )
        ),
        status=bot_data.get("status", ""),
        hearts=bot_data.get("hearts", 0),
        guilds=bot_data.get("guilds", 0),
        category=list(
            map(
                lambda category: types.Category(
                    category.get("label", ""),
                ),
                bot_data.get("category", []),
            )
        ),
        website=bot_data.get("website", ""),
        support=bot_data.get("support", ""),
        github=bot_data.get("github", ""),
        banner=bot_data.get("banner", ""),
        state=bot_data.get("state", ""),
        badges=bot_data.get("badges", []),
        locked=bot_data.get("locked", False),
    )


@pytest.fixture
def user_data():
    return User(
        id=user_data.get("userid", 0),
        username=user_data.get("username", ""),
        descriminator=user_data.get("discriminator", ""),
        avatar=user_data.get("useravatar", ""),
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
                            lambda category: types.Category(
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
                user_data.get("bots", []),
            )
        ),
        badges=user_data.get("badges", []),
    )


@pytest.fixture
def vote_data():
    return Vote(
        voted=True if vote_data.get("status", 0) == 200 else False,
    )
