from dataclasses import dataclass


class B:
    def __init__(self, x: int, y: str = "hello", l: list[int] | None = None) -> None:
        self.x = x
        self.y = y
        self.l = [] if not l else l


@dataclass
class DcB:
    x: int
    y: str = "hello"
    l: list[int] | None = None

    def __post_init__(self):
        self.l: list[int] | None = [] if not self.l else self.l

    # @property
    # def l(self) -> list[int] | None:
    #     return [] if not self._l else self._l


def main():
    original = B(1)
    dc_b = DcB(x=1)
    assert type(original.l) == type(dc_b.l)
    assert len(original.l) == len(dc_b.l)

    original.l += "a"
    assert len(original.l) != len(dc_b.l)

    assert original.x == dc_b.x

    original.x = 2
    dc_b.x = 2
    assert original.x == dc_b.x

    assert original.y == dc_b.y

    original.y = "world"
    dc_b.y = "world"
    assert original.y == dc_b.y


main()
