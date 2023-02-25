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

    EDGE = "edge"

    IPHONE11 = "iphone11"
    IPHONE12 = "iphone12"
    IPHONE13 = "iphone13"

    S20 = "S20"
    S21 = "S21"
    S22 = "S22"
    S23 = "S23"


@dataclass
class Phone:
    brand: PhoneBrand = PhoneBrand.DEFAULT
    model: PhoneTypes = PhoneTypes.DEFAULT
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

        raise TypeError(f"{self.model} not valid")

    def get_serial(self) -> int:
        import datetime

        return int(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))

    def __post_init__(self):
        self.serial_number = self.get_phone_prefix() + str(self.get_serial())
