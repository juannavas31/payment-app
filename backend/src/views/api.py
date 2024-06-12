import requests
from fastapi import APIRouter, Depends, Request

from src.settings import Settings, get_settings

api_router = APIRouter()

def payments_url(settings: Settings) -> str:
    return f'http://{settings.PAYMENT_API_HOST}:{settings.PAYMENT_API_PORT}/api/payments'

@api_router.get('/')
async def get_index():
    return {
        'service': 'backend:api',
        'ok': True
    }

@api_router.get('/payments')
async def get_payments(settings: Settings = Depends(get_settings)):
    print("api-key", settings.API_KEY)
    response = requests.get(
        url=payments_url(settings),
        headers={'x-api-key': settings.API_KEY},
        timeout=settings.UPSTREAM_REQUEST_TIMEOUT
    )
    response.raise_for_status()
    return response.json()

@api_router.post('/payments')
async def post_payments(
    request: Request,
    settings: Settings = Depends(get_settings)
):
    json = await request.json()
    response = requests.post(
        url=payments_url(settings),
        headers={'Content-Type': 'application/json', 'x-api-key': settings.API_KEY},
        json=json,
        timeout=settings.UPSTREAM_REQUEST_TIMEOUT
    )
    response.raise_for_status()
    return response.json()
