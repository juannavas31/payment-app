from fastapi import FastAPI

from src.views.api import api_router
from src.views.index import index_router

app = FastAPI()
app.include_router(index_router)
app.include_router(api_router, prefix='/api')
