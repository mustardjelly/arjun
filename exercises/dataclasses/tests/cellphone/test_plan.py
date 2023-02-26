import datetime
from freezegun import freeze_time
from exercises.dataclasses.cellphone.customer import Customer
from exercises.dataclasses.cellphone.phones import Phone, PhoneTypes
from exercises.dataclasses.cellphone.plan import Plan


def test_initialize():
    cust = Customer(
        "Sam Powell", "44 St Lukes Rd, Mt Royale, 1025", "real_email@gmail.com"
    )
    phone = Phone(model=PhoneTypes.IPHONE13, price=2699.97)
    with freeze_time("2022-12-31"):
        plan = Plan(cust, phone)

        assert plan.start_date == datetime.datetime.now()


def test_initialize_date():
    cust = Customer(
        "Sam Powell", "44 St Lukes Rd, Mt Royale, 1025", "real_email@gmail.com"
    )
    phone = Phone(model=PhoneTypes.IPHONE13, price=2699.97)

    with freeze_time("2022-12-31"):
        now = datetime.datetime.now()
        with freeze_time("2023-01-01"):
            plan = Plan(cust, phone, now)

            assert plan.start_date == now
            assert plan.start_date != datetime.datetime.now()
