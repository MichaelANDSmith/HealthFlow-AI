from app.models.time_management import generate_daily_schedule

def get_user_schedule(user_data):
    """
    Fetch the user's personalized daily schedule.
    :param user_data: The data of the user (e.g., work, study, and break times)
    :return: A dictionary with the user's schedule for the day
    """
    schedule = generate_daily_schedule(user_data)
    return schedule
    
def save_user_schedule_to_db(user_id, user_data): 
    """
    Save the user's daily schedule to the database.
    :param user_id: The unique ID of the user
    :param user_data: The data of the user for schedule generation
    :return: A confirmation message
    """
    schedule = get_user_schedule(user_data)  # Source Code Reuse
    save_user_schedule(user_id=user_id, schedule=schedule)  
    return f"Schedule for user {user_id} saved successfully." 

def fetch_user_schedule_history(user_id): 
    """
    Fetch the history of saved schedules for a user.
    :param user_id: The unique ID of the user
    :return: A list of past schedules
    """
    history = get_schedule_history(user_id)  
    if not history:  
        return f"No schedule history found for user {user_id}." 
    return history 
