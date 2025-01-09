from flask import Blueprint, request, jsonify
from app.services.health_advice import get_user_health_advice

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
