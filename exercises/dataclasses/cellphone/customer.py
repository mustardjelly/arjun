"""
customers (name, address, email address)
"""

from dataclasses import dataclass


@dataclass
class Customer:
    name: str = ""
    address: str = ""
    email_address: str = ""
