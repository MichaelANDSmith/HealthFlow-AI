import random

def get_health_advice(user_profile):
    """
    Provide personalized health advice based on the user's health data.
    :param user_profile: User's health data (e.g., age, activity level, diet)
    :return: A string with health advice
    """
    advice_list = [
        "Drink plenty of water throughout the day.",
        "Make sure to get at least 30 minutes of exercise daily.",
        "Ensure you're eating a balanced diet with lots of fruits and vegetables."
    ]
    return random.choice(advice_list)
