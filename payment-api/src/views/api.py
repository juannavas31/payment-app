from fastapi import APIRouter

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


@api_router.get('/payments')
async def get_payments():
    return ALL_PAYMENTS


@api_router.post('/payments')
async def post_payments():
    raise NotImplementedError()
