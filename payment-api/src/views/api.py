from fastapi import FastAPI, APIRouter, Depends, HTTPException, status, Header
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv('../../../.env')

# Define a Pydantic model that represents the structure of the payment data
class Payment(BaseModel):
    id: str
    name: str
    cardNumber: str
    currency: str
    amount: str


# A fake database of payments.
# 
# Each payment is identified by its `id`. All fields are required.
#
# Modifying `ALL_PAYMENTS` is ok for the purposes of the test.
ALL_PAYMENTS = [
    {
        'id': 'example-a',
        'name': 'Anne Alpaca',
        'cardNumber': '1111222233334444',
        'currency': 'GBP',
        'amount': '1.23',
    },
    {
        'id': 'example-b',
        'name': 'Ben Bear',
        'cardNumber': '2222333344445555',
        'currency': 'EUR',
        'amount': '2.34',
    },
    {
        'id': 'example-c',
        'name': 'Carol Crane',
        'cardNumber': '2222333344445555',
        'currency': 'EUR',
        'amount': '2.34',
    },
]

api_router = APIRouter()

# Define a dependency function
def get_api_key(x_api_key: str = Header(None)):
    expected_api_key = os.getenv("API_KEY")
    if x_api_key != expected_api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
        )
    
@api_router.get('/payments')
async def get_payments(x_api_key: str = Depends(get_api_key)):
    return ALL_PAYMENTS

    @api_router.post('/payments')
    async def post_payments(payment: Payment, x_api_key: str = Depends(get_api_key)):

        payment = await request.json()
        # Now `payment` is a Pydantic model instance with the request body data
        # Convert model instance to dict and append to ALL_PAYMENTS
        ALL_PAYMENTS.append(payment.dict())
        return {'message': 'Payment saved successfully'}

    
