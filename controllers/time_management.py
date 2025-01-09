from flask import Blueprint, request, jsonify
from app.services.time_management import get_user_schedule

bp = Blueprint('time', __name__, url_prefix='/time')

@bp.route('/get_schedule', methods=['POST'])
def get_schedule():
    """
    API endpoint to get the user's daily schedule.
    :return: A JSON response with the personalized schedule
    """
    user_data = request.get_json()
    schedule = get_user_schedule(user_data)
    return jsonify(schedule)
