from pydantic import BaseModel


class RecommendationRequest(BaseModel):
    """
    Модель запроса для получения рекоммендации
    """
    user_id: int
