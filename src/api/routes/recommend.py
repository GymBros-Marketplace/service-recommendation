from fastapi import APIRouter, HTTPException
from src.schemas.requests import RecommendationRequest
from src.services.recommendation import generate_recommendations
import logging

router = APIRouter()

logging.basicConfig(level=logging.INFO)


@router.post("/recommend/")
async def recommend(request: RecommendationRequest):
    """
    Рекоммендация товаров пользователю
    """
    logging.info(f"Пришел запрос: {request}")

    try:
        user_id = request.user_id
        recommendations = generate_recommendations(user_id)
        return {"recommendations": recommendations}
    except Exception as e:
        logging.error(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")