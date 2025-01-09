from app.models.time_management import generate_daily_schedule

def get_user_schedule(user_data):
    """
    Fetch the user's personalized daily schedule.
    :param user_data: The data of the user (e.g., work, study, and break times)
    :return: A dictionary with the user's schedule for the day
    """
    schedule = generate_daily_schedule(user_data)
    return schedule
