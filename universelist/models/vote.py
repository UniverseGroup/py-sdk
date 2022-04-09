from dataclasses import dataclass


@dataclass(frozen=True)
class Vote:
    voted: bool

    def __init__(self, data: dict) -> None:
        super().__init__(
            voted=True if data.get("status") == 200 else False,
        )
