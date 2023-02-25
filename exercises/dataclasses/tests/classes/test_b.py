import pytest

from classes.b import DcB, B


def test_initialize():
    original = B(1)
    dataclass = DcB(1)

    assert original.x == dataclass.x
    assert original.y == dataclass.y
    assert type(original.l) == type(dataclass.l)
    assert len(original.l) == len(dataclass.l)
    assert original.l == dataclass.l


@pytest.mark.parametrize(
    "int_to_set, str_to_set, number_of_items", [(3, "world", 3), (0, "", 0)]
)
def test_initialize_values(int_to_set: int, str_to_set: str, number_of_items: int):
    original = B(int_to_set, str_to_set, [str(num) for num in range(number_of_items)])
    dataclass = DcB(
        int_to_set, str_to_set, [str(num) for num in range(number_of_items)]
    )

    assert original.x == dataclass.x == int_to_set
    assert original.y == dataclass.y == str_to_set
    assert type(original.l) == type(dataclass.l)
    assert len(original.l) == len(dataclass.l)
    assert original.l == dataclass.l


@pytest.mark.parametrize("int_to_set", range(-1, 2))
@pytest.mark.parametrize("str_to_set", [("world"), ("")])
@pytest.mark.parametrize("init_list", [(3), (2)])
def test_set_values(int_to_set: int, str_to_set: str, init_list: int):
    o_list = [number for number in range(init_list)]
    dc_list = [number for number in range(init_list)]
    original = B(1)
    dataclass = DcB(1)

    original.x = int_to_set
    dataclass.x = int_to_set
    assert original.x == dataclass.x

    original.y = str_to_set
    dataclass.y = str_to_set
    assert original.y == dataclass.y

    original.l = o_list
    dataclass.l = dc_list
    assert original.l == dataclass.l
