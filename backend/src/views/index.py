from typing import Union

from fastapi import APIRouter

index_router = APIRouter()


@index_router.get('/')
async def get_index():
    return {
        'service': 'backend',
        'ok': True
    }
