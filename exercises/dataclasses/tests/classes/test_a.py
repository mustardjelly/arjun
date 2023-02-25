import pytest

from classes.a import DcA, A


def test_initialize():
    original = A()
    dataclass = DcA()

    assert original._length == dataclass._length


@pytest.mark.parametrize("length_to_set", [(0), (10), (-10)])
def test_initialize_with_val(length_to_set: int):
    original = A()
    dataclass = DcA()

    assert original._length == dataclass._length
