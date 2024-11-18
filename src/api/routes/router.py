from fastapi import APIRouter
from src.api.routes import recommend
from src.api.routes import (
    healthcheck,
)

router = APIRouter()

router.include_router(recommend.router, tags=["recommend"])
router.include_router(healthcheck.router, tags=["healthcheck"])
