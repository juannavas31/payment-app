from fastapi import APIRouter

index_router = APIRouter()


@index_router.get('/')
async def get_index():
    return {
        'service': 'payment-api',
        'ok': True
    }
