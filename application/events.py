import logging
import typing

from application.core import config

if typing.TYPE_CHECKING:
    from fastapi import FastAPI

logger = logging.getLogger(__name__)


def register_events(app: 'FastAPI') -> None:
    @app.on_event('startup')
    async def startup_event() -> None:  # pyright: ignore
        print('Startup event')

    @app.on_event('shutdown')
    async def shutdown_event() -> None:  # pyright: ignore
        print('Shutdown event')