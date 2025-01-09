from flask import Blueprint, request, jsonify
from app.services.user_service import register_user, authenticate_user

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    new_user = register_user(username, email, password)
    return jsonify({"message": f"User {new_user.username} created successfully"}), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    token = authenticate_user(email, password)
    if token:
        return jsonify(access_token=token)
    return jsonify({"message": "Invalid credentials"}), 401
