import typing

import pytest
from asgi_lifespan import LifespanManager
from httpx import AsyncClient


if typing.TYPE_CHECKING:
    from collections.abc import AsyncGenerator

    from fastapi import FastAPI


@pytest.fixture(scope='session')
def app() -> 'FastAPI':
    from application.main import get_application

    return get_application()


@pytest.fixture(scope='session')
async def initialize_app(app: 'FastAPI') -> 'AsyncGenerator[FastAPI, None]':
    async with LifespanManager(app):
        yield app


@pytest.fixture(scope='session')
async def client(
    initialize_app: 'FastAPI',
) -> 'AsyncGenerator[AsyncClient, None]':
    async with AsyncClient(
        app=initialize_app,
        base_url='http://test-server.com',
        headers={'Content-Type': 'application/json'},
    ) as client:
        yield client
