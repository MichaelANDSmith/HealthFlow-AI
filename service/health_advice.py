from app.models.health_advice import get_health_advice, store_user_advice
from datetime import datetime

def get_user_health_advice(user_profile):
    """
    Fetch personalized health advice for the user.
    :param user_profile: The health data of the user (e.g., age, lifestyle)
    :return: A string with health advice
    """
    advice = get_health_advice(user_profile)
    return advice
    
def save_user_health_advice(user_id, user_profile):
    """
    Save personalized health advice for the user to the database.
    :param user_id: The unique ID of the user
    :param user_profile: The health data of the user
    :return: A confirmation message
    """
    advice = get_user_health_advice(user_profile)
    timestamp = datetime.now()

    # Save advice to the database
    store_user_advice(user_id=user_id, advice=advice, timestamp=timestamp)

    return f"Health advice for user {user_id} saved successfully at {timestamp}."

def display_user_advice_history(user_id):
    """
    Display the health advice history for the given user.
    :param user_id: The unique ID of the user
    :return: A list of health advice records
    """
    from app.models.health_advice import fetch_user_advice_history

    advice_history = fetch_user_advice_history(user_id)

    if not advice_history:
        return f"No health advice history found for user {user_id}."

    formatted_history = "\n".join(
        [f"Date: {record['timestamp']}, Advice: {record['advice']}" for record in advice_history]
    )
    return formatted_history
