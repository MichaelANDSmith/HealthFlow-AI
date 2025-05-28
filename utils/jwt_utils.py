from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request
from functools import wraps
from flask import jsonify
from app.models import User  # Assuming you have a User model

def get_current_user():
    """
    Get the currently logged-in user based on JWT identity.
    Returns the full user object with role checking and error handling.
    
    :return: User object if valid, None if invalid
    :raises: 401 Unauthorized if invalid token
    """
    try:
        # Verify the JWT is present and valid
        verify_jwt_in_request()
        
        # Get identity from token
        user_id = get_jwt_identity()
        
        if not user_id:
            return None
            
        # Fetch complete user from database
        user = User.query.get(user_id)
        
        if not user or not user.is_active:
            return None
            
        return user
        
    except Exception as e:
        # Log the error for debugging
        current_app.logger.error(f"Error getting current user: {str(e)}")
        return None

def admin_required(fn):
    """
    Decorator that requires the user to be an admin.
    Returns 403 Forbidden if user is not admin.
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        current_user = get_current_user()
        if not current_user or not current_user.is_admin:
            return jsonify({"msg": "Admin access required"}), 403
        return fn(*args, **kwargs)
    return wrapper

def get_current_user_id():
    """
    Lightweight version that just returns the user ID from JWT.
    Doesn't hit the database. Use when you only need the ID.
    
    :return: user_id or None if invalid
    """
    try:
        verify_jwt_in_request()
        return get_jwt_identity()
    except:
        return None

def user_required(fn):
    """
    Decorator that requires a valid logged-in user.
    Returns 401 Unauthorized if no valid user.
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        current_user = get_current_user()
        if not current_user:
            return jsonify({"msg": "Authentication required"}), 401
        return fn(*args, **kwargs)
    return wrapper
