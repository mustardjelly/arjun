# Class to change to dataclass, _length = 0
from dataclasses import dataclass


class A:
    def __init__(self) -> None:
        self._length = 0


@dataclass
class DcA:
    _length: int = 0


def main():
    original = A()
    dc_a = DcA()

    assert original._length == dc_a._length


main()
