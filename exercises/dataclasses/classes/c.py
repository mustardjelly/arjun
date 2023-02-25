from dataclasses import dataclass, field


class C:
    def __init__(self, a: int = 3) -> None:
        self.a = a
        self.b = a + 3


@dataclass
class DcC:
    a: int = 3
    b: int = field(init=False)

    def __post_init__(self) -> None:
        self.b = self.a + 3
