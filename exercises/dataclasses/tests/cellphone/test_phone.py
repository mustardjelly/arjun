from freezegun import freeze_time
import pytest
from exercises.dataclasses.cellphone import phones


@pytest.mark.parametrize(
    "expected_brand, phone_type",
    [
        (phones.PhoneBrand.APPLE, phones.PhoneTypes.IPHONE11),
        (phones.PhoneBrand.APPLE, phones.PhoneTypes.IPHONE12),
        (phones.PhoneBrand.APPLE, phones.PhoneTypes.IPHONE13),
        (phones.PhoneBrand.SAMSUNG, phones.PhoneTypes.S20),
        (phones.PhoneBrand.SAMSUNG, phones.PhoneTypes.S21),
        (phones.PhoneBrand.SAMSUNG, phones.PhoneTypes.S22),
        (phones.PhoneBrand.SAMSUNG, phones.PhoneTypes.S23),
        (phones.PhoneBrand.MOTOROLLA, phones.PhoneTypes.EDGE),
        (phones.PhoneBrand.DEFAULT, phones.PhoneTypes.DEFAULT),
    ],
)
@pytest.mark.parametrize("price", [(0.0), (100.0), (238.99)])
def test_initialize(
    expected_brand: phones.PhoneBrand, phone_type: phones.PhoneTypes, price: float
):
    mobile = phones.Phone(model=phone_type, price=price)

    assert mobile.brand == expected_brand
    assert mobile.model == phone_type
    assert mobile.price == price


def test_serial_generation_different():
    with freeze_time("2021-12-31"):
        mobile1 = phones.Phone(model=phones.PhoneTypes.S23, price=2199.00)

    with freeze_time("2012-01-14"):
        mobile2 = phones.Phone(model=phones.PhoneTypes.S23, price=2199.00)

    assert mobile1.serial_number != mobile2.serial_number


def test_serial_generation_same():
    with freeze_time("2021-12-31"):
        mobile1 = phones.Phone(model=phones.PhoneTypes.S23, price=2199.00)
        mobile2 = phones.Phone(model=phones.PhoneTypes.S23, price=2199.00)

    assert mobile1.serial_number == mobile2.serial_number
