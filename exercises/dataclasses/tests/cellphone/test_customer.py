import pytest
from exercises.dataclasses.cellphone.customer import Customer


@pytest.mark.parametrize(
    "name, address, email",
    [
        (
            "Sam Powell",
            "44 St Lukes Rd, Mt Albert, 1025",
            "muer.powell@gmail.com",
        ),
        (
            "Annemiek Powell",
            "44 St Lukes Rd, Mt Albert, 1025",
            "annemiekpowell@gmail.com",
        ),
    ],
)
def test_initialize(name: str, address: str, email: str):
    my_customer = Customer(name, address, email)

    assert my_customer.name == name
    assert my_customer.address == address
    assert my_customer.email_address == email
