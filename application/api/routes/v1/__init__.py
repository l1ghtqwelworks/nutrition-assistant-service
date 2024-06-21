from fastapi.routing import APIRouter

from application.api.routes.v1 import settings_route

router = APIRouter(tags=['Version 1'])

router.include_router(settings_route.router, prefix='/settings', tags=['settings'])

