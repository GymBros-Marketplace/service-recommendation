from fastapi import APIRouter
from src.schemas.healthcheck import HealthcheckResult
from src.services.utils import return_current_time

router = APIRouter()


@router.get("/healthcheck/", response_model=HealthcheckResult, name="healthcheck")
def get_health_check() -> HealthcheckResult:
    """
    Эндпоинт для проверки состояния
    """
    health_check = HealthcheckResult(is_alive=True, date=return_current_time())

    return health_check
