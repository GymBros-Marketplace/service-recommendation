from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes.router import router as api_router
from loguru import logger


def get_app() -> FastAPI:
    """
    Инициализация сервиса FastAPI
    """
    fastapi_app = FastAPI(
        title="Recommendation service",
        version="0.1.0",
        debug=False,
    )
    fastapi_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["GET", "POST"],
        allow_headers=["*"],
    )

    fastapi_app.include_router(api_router, prefix="/api")
    logger.info("FastAPI application has been initialized")
    return fastapi_app


app = get_app()
