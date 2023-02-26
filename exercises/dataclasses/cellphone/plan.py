"""
plans (which refer to a customer, a phone, a start date)
"""

from dataclasses import dataclass, field
from datetime import datetime

from exercises.dataclasses.cellphone.customer import Customer
from exercises.dataclasses.cellphone.phones import Phone, PhoneTypes


@dataclass
class Plan:
    customer: Customer
    phone: Phone
    start_date: datetime = field(default_factory=lambda: datetime.now())
