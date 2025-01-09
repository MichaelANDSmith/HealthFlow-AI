from app import celery
from app.models.time_management import generate_daily_schedule
import time

@celery.task
def async_generate_schedule(user_data):
    """
    Async task to generate a personalized schedule.
    :param user_data: User data (e.g., work hours, preferences)
    :return: A personalized daily schedule
    """
    time.sleep(5)  # Simulate time-consuming task
    return generate_daily_schedule(user_data)
