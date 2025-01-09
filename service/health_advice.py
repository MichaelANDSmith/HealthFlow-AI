from app.models.health_advice import get_health_advice

def get_user_health_advice(user_profile):
    """
    Fetch personalized health advice for the user.
    :param user_profile: The health data of the user (e.g., age, lifestyle)
    :return: A string with health advice
    """
    advice = get_health_advice(user_profile)
    return advice
