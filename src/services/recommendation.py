from src.services.model import get_user_features, get_all_products, predict

def generate_recommendations(user_id: int):
    user_features = get_user_features(user_id)
    products = get_all_products()
    predictions = predict(user_features, products)
    return predictions