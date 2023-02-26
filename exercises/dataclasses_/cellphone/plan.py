"""
plans (which refer to a customer, a phone, a start date)
"""

from dataclasses import dataclass, field
from datetime import datetime

from exercises.dataclasses_.cellphone.customer import Customer
from exercises.dataclasses_.cellphone.phones import Phone, PhoneTypes


@dataclass
class Plan:
    customer: Customer
    phone: Phone
    start_date: datetime = field(default_factory=lambda: datetime.now())


customer = Customer("Sam", "My addy", "email@email.com")
phone = Phone(model=PhoneTypes.IPHONE13, price=2399.99)
