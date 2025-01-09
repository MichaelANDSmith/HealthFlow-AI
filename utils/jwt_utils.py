from flask_jwt_extended import get_jwt_identity

def get_current_user():
    """
    Get the currently logged-in user based on JWT identity.
    :return: User's ID
    """
    user_id = get_jwt_identity()
    return user_id
