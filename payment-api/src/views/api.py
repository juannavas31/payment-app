from typing import Optional
from fastapi import FastAPI, APIRouter, Depends, HTTPException, status, Header
from pydantic import BaseModel
from dotenv import load_dotenv, dotenv_values
import os
import json
import random
import string

load_dotenv('../../.env')

# Define a Pydantic model that represents the structure of the payment data
class Payment(BaseModel):
    id: Optional[str] = None
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

def generate_unique_id(length=7):
    chars = string.ascii_letters + string.digits
    unique_id = ''.join(random.choice(chars) for _ in range(length))
    return unique_id

def search_payment_by_id(payment_id: str):
    for payment in ALL_PAYMENTS:
        if payment['id'] == payment_id:
            return payment
    return None

api_router = APIRouter()

# Define a dependency function
def get_api_key(x_api_key: str = Header(None)):
    config_api = dotenv_values("./.env")
    expected_api_key = config_api["API_KEY"]
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
    print("Entering post_payments")
    print("payment received", json.dumps(payment.dict()))
    # payment = await request.json()
    # Now `payment` is a Pydantic model instance with the request body data
    # Convert model instance to dict and append to ALL_PAYMENTS
    payment_id = generate_unique_id()
    while search_payment_by_id(payment_id) is not None:
        payment_id = generate_unique_id()
    payment_dict = payment.dict()
    payment_dict['id'] = payment_id
    print("storing payment ", json.dumps(payment_dict))
    ALL_PAYMENTS.append(payment_dict)
    return {'message': 'Payment saved successfully'}

    
