from datetime import date, datetime, timedelta
from starkbank import Invoice as StarkInvoice
from app.models import Person
from decimal import Decimal
from typing import Union
import random

class Invoice:
    invoice_created: StarkInvoice = None
    amount: int = 0,
    due: datetime = (datetime.now() + timedelta(days=1)).date(),
    tax_id: str = None,
    name: str = None,
    expiration: Union[datetime, int] = 123456789,
    fine: Decimal = 2.5,
    interest: Decimal = 1.3,
    discounts: list[dict] = [
        {
            "percentage": 2,
            "due": (datetime.now() + timedelta(days=1)).date()
        }
    ],
    tags: list[str] = [
        "test",
        "gabriel nori"
    ],
    descriptions: list[dict] = [
        {
            "key": "Origin",
            "value": "Gabriel Nori"
        },
        {
            "key": "Reason",
            "value": "Hiring process"
        }
    ]

    def __init__(self) -> None:
        pass

    def create(self, ammount: int, payer: Person):
        self.invoice_created = StarkInvoice(
            amount = ammount,
            tax_id = payer.cpf,
            name = payer.name,
            due=self.due,
            expiration=self.expiration,
            fine=self.fine,
            interest=self.interest,
        )
    

    def generate_random(self):
        person = Person()
        person.set_random()

        self.create(
            random.randint(100, 10000000),
            person
        )