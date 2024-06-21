from fastapi.routing import APIRouter

from application.api.routes import v1

router = APIRouter()

router.include_router(v1.router, prefix='/v1')
