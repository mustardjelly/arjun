"""
plans (which refer to a customer, a phone, a start date)
"""

from dataclasses import dataclass
from datetime import datetime

from exercises.dataclasses.cellphone.customer import Customer
from exercises.dataclasses.cellphone.phones import Phone


@dataclass
class Plan:
    customer: Customer
    phone: Phone
    start_date: datetime
