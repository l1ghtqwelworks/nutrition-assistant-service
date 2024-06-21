import logging

from fastapi import FastAPI

from application import api, events
from application.core import config


logging.basicConfig(
    format='%(asctime)s.%(msecs)03d | %(levelname)-8s | %(filename)s:%(funcName)s:%(lineno)d - %(message)s',
    level=logging.INFO,
    datefmt='%F %T',
)


def get_application() -> FastAPI:
    application = FastAPI(**config.fastapi_kwargs)
    application.include_router(api.router, prefix=config.api_prefix)
    events.register_events(application)

    return application


app = get_application()
