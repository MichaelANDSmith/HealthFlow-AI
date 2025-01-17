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
    # Customizing advice based on user profile (Example)
    if user_profile.get("age") > 50:
        advice_list.append("Consider regular health check-ups for better aging.")
    if user_profile.get("activity_level") == "low":
        advice_list.append("Start with light activities like walking to improve your fitness.")
        
    return random.choice(advice_list)
