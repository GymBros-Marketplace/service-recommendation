from loguru import logger
from datetime import datetime


async def print_logger_info(user_id: str, predicted):
    """
    Логгирование предсказания
    """
    logger.info({"user_id": user_id, "predicted": predicted})


def return_current_time():
    """
    Для проверки состояния
    """
    return datetime.now().isoformat()
