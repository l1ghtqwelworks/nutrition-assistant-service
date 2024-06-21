import logging

from fastapi.routing import APIRouter

from application.api import routes


logger = logging.getLogger(__name__)

router = APIRouter()


router.include_router(
    routes.router
)


@router.get('/health', include_in_schema=False)
async def health() -> dict[str, str]:
    # TODO check the health of the sms service
    return {'status': 'ok'}
