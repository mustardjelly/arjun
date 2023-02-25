import pytest
from exercises.dataclasses.cellphone import phones


@pytest.mark.parametrize(
    "phone_brand, phone_type",
    [
        (phones.PhoneBrand.APPLE, phones.PhoneTypes.IPHONE11),
        (phones.PhoneBrand.APPLE, phones.PhoneTypes.IPHONE12),
        (phones.PhoneBrand.APPLE, phones.PhoneTypes.IPHONE13),
        (phones.PhoneBrand.SAMSUNG, phones.PhoneTypes.S20),
        (phones.PhoneBrand.SAMSUNG, phones.PhoneTypes.S21),
        (phones.PhoneBrand.SAMSUNG, phones.PhoneTypes.S22),
        (phones.PhoneBrand.SAMSUNG, phones.PhoneTypes.S23),
        (phones.PhoneBrand.MOTOROLLA, phones.PhoneTypes.EDGE),
    ],
)
@pytest.mark.parametrize("price", [(0.0), (100.0), (238.99)])
def test_initialize(
    phone_brand: phones.PhoneBrand, phone_type: phones.PhoneTypes, price: float, freezer
):
    mobile = phones.Phone(brand=phone_brand, model=phone_type, price=price)

    assert mobile.brand == phone_brand
    assert mobile.model == phone_type
    assert mobile.price == price


# Serial tests
