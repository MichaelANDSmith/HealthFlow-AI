from app.models.time_management import generate_daily_schedule, save_user_schedule, get_schedule_history, delete_schedule, update_schedule, clear_schedule_history  

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
 
def delete_user_schedule(user_id, schedule_id):
    """
    Delete a specific schedule for a user.
    :param user_id: The unique ID of the user
    :param schedule_id: The ID of the schedule to delete
    :return: A confirmation message
    """
    success = delete_schedule(user_id, schedule_id)
    if success:
        return f"Schedule {schedule_id} for user {user_id} deleted successfully."
    return f"Failed to delete schedule {schedule_id} for user {user_id}."
 
def update_user_schedule(user_id, schedule_id, new_data):
    """
    Update an existing schedule for a user.
    :param user_id: The unique ID of the user
    :param schedule_id: The ID of the schedule to update
    :param new_data: The updated schedule data
    :return: A confirmation message
    """
    updated_schedule = update_schedule(user_id, schedule_id, new_data)
    if updated_schedule:
        return f"Schedule {schedule_id} for user {user_id} updated successfully."
    return f"Failed to update schedule {schedule_id} for user {user_id}."

def clear_user_schedule_history(user_id):
    """
    Clear all saved schedule history for a user.
    :param user_id: The unique ID of the user
    :return: A confirmation message
    """
    success = clear_schedule_history(user_id)
    if success:
        return f"All schedule history for user {user_id} cleared successfully."
    return f"Failed to clear schedule history for user {user_id}."
    history = get_schedule_history(user_id)  
    if not history:  
        return f"No schedule history found for user {user_id}." 
    return history 
