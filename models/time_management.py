import numpy as np

def generate_daily_schedule(user_data):
    """
    Generate a personalized daily schedule based on the user's needs.
    :param user_data: User data containing daily requirements (e.g., work hours, break times)
    :return: A personalized daily schedule
    """
    # Default schedule as fallback
    schedule = {
        "morning": "Work on project",
        "afternoon": "Take a break and do some exercise",
        "evening": "Relax and meditate"
    }

    # Extract user preferences if available
    work_hours = user_data.get("work_hours", 4)
    break_time = user_data.get("break_time", 1)
    evening_activity = user_data.get("evening_activity", "Relax and meditate")

    # Randomly shuffle afternoon activities to introduce variety
    activities = ["Take a walk", "Do yoga", "Stretching", "Short nap"]
    np.random.seed(42)  # For reproducibility
    afternoon_task = np.random.choice(activities)

    # Build personalized schedule
    schedule["morning"] = f"Work for {work_hours} hours on key tasks"
    schedule["afternoon"] = f"{afternoon_task} for {break_time} hour(s)"
    schedule["evening"] = evening_activity

    return schedule
