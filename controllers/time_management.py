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

@bp.route('/update_schedule', methods=['PUT'])
def update_schedule():
    """
    API endpoint to update a user's schedule.
    :return: A JSON response indicating success or failure
    """
    data = request.get_json()
    success = update_user_schedule(data)
    if success:
        return jsonify({"message": "Schedule updated successfully"}), 200
    else:
        return jsonify({"error": "Failed to update schedule"}), 400

@bp.route('/delete_schedule', methods=['DELETE'])
def delete_schedule():
    """
    API endpoint to delete a user's schedule entry.
    :return: A JSON response indicating success or failure
    """
    data = request.get_json()
    success = delete_user_schedule(data)
    if success:
        return jsonify({"message": "Schedule entry deleted successfully"}), 200
    else:
        return jsonify({"error": "Failed to delete schedule entry"}), 400

@bp.route('/add_schedule_entry', methods=['POST'])
def add_schedule_entry():
    """
    API endpoint to add a new entry to the user's schedule.
    :return: A JSON response indicating success or failure
    """
    data = request.get_json()
    success = add_user_schedule_entry(data)
    if success:
        return jsonify({"message": "Schedule entry added successfully"}), 201
    else:
        return jsonify({"error": "Failed to add schedule entry"}), 400
