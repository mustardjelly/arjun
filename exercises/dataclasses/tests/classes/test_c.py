import pytest

from classes.c import C, DcC


def test_initialize():
    original = C()
    dataclass = DcC()

    assert original.a == dataclass.a
    assert original.b == dataclass.b


@pytest.mark.parametrize("a_value", range(11))
def test_initialize_value(a_value: int):
    original = C(a_value)
    dataclass = DcC(a_value)

    assert original.a == dataclass.a
    assert original.b == dataclass.b


@pytest.mark.parametrize("a_value", range(3))
@pytest.mark.parametrize("b_value", range(3))
def test_initialize_value_all(a_value: int, b_value: int):
    original = C(b_value)
    dataclass = DcC(b_value)

    original.a = a_value
    dataclass.a = a_value

    original.b = b_value
    dataclass.b = b_value

    assert original.a == dataclass.a
    assert original.b == dataclass.b
