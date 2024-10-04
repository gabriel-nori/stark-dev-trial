from datetime import date, datetime, timedelta
from decimal import Decimal
from typing import Union

class Invoice:
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
    tags: list[str] = [],
    descriptions: list[dict] = [
        # {
        #     "key": "Field1",
        #     "value": "Something"
        # }
    ]

    def __init__(self) -> None:
        pass