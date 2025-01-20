from flask import Blueprint, request, jsonify
from app.services.health_advice import get_user_health_advice,save_user_health_advice_to_db

bp = Blueprint('health', __name__, url_prefix='/health')

@bp.route('/get_health_advice', methods=['POST'])
def get_health():
    """
    API endpoint to get personalized health advice for the user.
    :return: A JSON response with health advice
    """
    user_profile = request.get_json()
    advice = get_user_health_advice(user_profile)
    return jsonify({"advice": advice})

@bp.route('/save_health_advice', methods=['POST'])
def save_health():
    """
    API endpoint to save the user's personalized health advice to the database.
    :return: A JSON response confirming the save operation
    """
    user_profile = request.get_json()
    user_id = user_profile.get("user_id")  # Assuming user_profile includes user_id
    save_user_health_advice_to_db(user_id, user_profile)
    return jsonify({"message": f"Health advice for user {user_id} saved successfully."})
