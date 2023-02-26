"""
phones (brand, model, price, serial number) 
"""
from dataclasses import dataclass, field
from enum import Enum


class PhoneBrand(Enum):
    APPLE = "Apple"
    SAMSUNG = "Samsung"
    MOTOROLLA = "Motorolla"
    DEFAULT = "Default"


class PhoneTypes(Enum):
    DEFAULT = "Default"

    # Motorolla
    EDGE = "edge"

    # Apple
    IPHONE11 = "iphone11"
    IPHONE12 = "iphone12"
    IPHONE13 = "iphone13"

    # Samsung
    S20 = "S20"
    S21 = "S21"
    S22 = "S22"
    S23 = "S23"


PHONE_MAPPING: dict = {
    PhoneTypes.EDGE: PhoneBrand.MOTOROLLA,
    PhoneTypes.IPHONE11: PhoneBrand.APPLE,
    PhoneTypes.IPHONE12: PhoneBrand.APPLE,
    PhoneTypes.IPHONE13: PhoneBrand.APPLE,
    PhoneTypes.S20: PhoneBrand.SAMSUNG,
    PhoneTypes.S21: PhoneBrand.SAMSUNG,
    PhoneTypes.S22: PhoneBrand.SAMSUNG,
    PhoneTypes.S23: PhoneBrand.SAMSUNG,
    PhoneTypes.DEFAULT: PhoneBrand.DEFAULT,
}


@dataclass
class Phone:
    model: PhoneTypes = PhoneTypes.DEFAULT
    brand: PhoneBrand = PhoneBrand.DEFAULT
    price: float = 0.0
    serial_number: str = ""

    def get_phone_prefix(self):
        if not self.model:
            raise ValueError(f"self.modle not defined")

        if self.brand == PhoneBrand.MOTOROLLA:
            return "M"

        if self.brand == PhoneBrand.APPLE:
            return "A"

        if self.brand == PhoneBrand.SAMSUNG:
            return "S"

        if self.brand == PhoneBrand.DEFAULT:
            return "D"

        raise TypeError(f"{self.model} not valid")

    def get_serial(self) -> int:
        import datetime

        return int(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))

    def get_phone_brand(self) -> PhoneBrand:
        if not self.model:
            raise ValueError("Model is unset")

        phone_brand: PhoneBrand = PHONE_MAPPING.get(self.model)

        if not phone_brand:
            raise TypeError(f"Phone model: {self.model}")

        return phone_brand

    def __post_init__(self):
        self.brand = self.get_phone_brand()
        self.serial_number = self.get_phone_prefix() + str(self.get_serial())
