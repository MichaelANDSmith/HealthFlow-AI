from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User
from app import db
from flask_jwt_extended import create_access_token

def register_user(username, email, password):
    """
    Register a new user and hash the password.
    :param username: User's username
    :param email: User's email address
    :param password: User's password
    :return: User object
    """
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, email=email, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def authenticate_user(email, password):
    """
    Authenticate user and return JWT if valid.
    :param email: User's email
    :param password: User's password
    :return: JWT token if valid
    """
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password_hash, password):
        access_token = create_access_token(identity=user.id)
        return access_token
    return None
