from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    PAYMENT_API_HOST: str = Field(
        env='PAYMENT_API_HOST',
        default='localhost'
    )
    PAYMENT_API_PORT: str = Field(
        env='PAYMENT_API_PORT',
        default='3002'
    )
    UPSTREAM_REQUEST_TIMEOUT: int = Field(
        env='UPSTREAM_REQUEST_TIMEOUT',
        default=10
    )


def get_settings() -> Settings:
    return Settings()
