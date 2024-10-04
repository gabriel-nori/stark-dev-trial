from fastapi_utilities import repeat_every
from app.config import settings
from app.models import Invoice
from app.logger import Logger
from fastapi import FastAPI
import starkbank
import random

logger = Logger("main")

logger.info("Application is starting...")


logger.info("Creating Stark project credentials")

project = starkbank.Project(
    id = settings.PROJECT_ID,
    environment = "sandbox",
    private_key = settings.PRIVATE_KEY
)

"""
Steps to be implemented:

The written code must be able to achieve three different steps:

1-> Send a API post to create between 8 and 12 invoices every 3 hours for 24 hours (8 interactions)
    --> Important!!: Since this application is not supposed to be ran for more than the test interval, I'm going
    to use fastAPI's cron instead of deploying a full infrastructure to run Celery or aio.
    Celery can handle concurrency and multiple tasks running in parallel through multiple workers.
    If this was a real world application, I would set a server for each micro service and then after they received
    a task that needs further processing I would insert it into a celery queue by its priority (3 minimum: High, Medium, Low)
    and each one of them having different scaling policies (GKE/EKS) to optimize cost without hurting performance.
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
    Create API request to create a new invoice -> Done
    Create cron to execute the API call -> Done
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

@app.on_event('startup')
@repeat_every(seconds=3*60*60, max_repetitions=8, raise_exceptions=True)
async def create_invoices():
    logger.info("starting invoice creation")
    invoices: list[Invoice] = []
    for i in range(random.randint(8,12)):
        invoice = Invoice()
        invoice.generate_random()
        invoices.append(invoice)

    logger.debug("invoices objects created. Sending to the API")

    for invoice_obj in invoices:
        try:
            created_invoices = starkbank.invoice.create([invoice_obj.invoice_created], user=project)
            logger.debug(
                "Invoices created by the API",
                extra={
                    "invoice": str(created_invoices)
                }
            )
        except Exception as e:
            logger.error(
                "Failed to create invoice",
                extra={
                    "exception": str(e)
                }
            )