from app.config import settings
from fastapi import FastAPI

"""
Steps to be implemented:

The written code must be able to achieve three different steps:

1-> Send a API post to create between 8 and 12 invoices every 3 hours for 24 hours (8 interactions)
2-> Receive an API post (webhook callback) whenever an invoice is payed
3-> Tranfer the money to the Stark Bank account, retaining the processing taxes:
    bank code: 20018183
    branch: 0001
    account: 6341320293482496
    name: Stark Bank S.A.
    tax ID: 20.018.183/0001-80
    account type: payment
    taxes:
        processing: 0,15
        liquidation: 0,50
        total: 0,65
    
steps left:
    Generate random CPF to create an invoice (tax_id) -> Done
    Create Person model -> Done
    Create invoice model -> Done
    Create API request to create a new invoice
    Create cron to execute the API call
    Create endpoint to receive callbacks
    Create unit test for:
        Person model
        Invoice model
        Invoice callback
"""


app = FastAPI()


@app.get("/callback/")
def handle_callback():
    a=1