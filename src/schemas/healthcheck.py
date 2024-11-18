from pydantic import BaseModel


class HealthcheckResult(BaseModel):
    """
    Модель запроса для проверки состояния сервиса
    """
    is_alive: bool
    date: str
