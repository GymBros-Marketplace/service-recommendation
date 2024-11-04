from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict
import random

app = FastAPI()

class RecommendationRequest(BaseModel):
    user_id: int
    item_ids: List[int]

class ItemRating(BaseModel):
    item_id: int
    rating: float

@app.post("/recommendations/", response_model=List[ItemRating])
async def get_recommendations(request: RecommendationRequest):
    recommendations = [
        {"item_id": item_id, "rating": round(random.uniform(1, 5), 2)}
        for item_id in request.item_ids
    ]
    return recommendations
