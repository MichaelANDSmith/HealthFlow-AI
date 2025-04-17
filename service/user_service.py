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
    if User.query.filter_by(email=email).first():
        return {'error': 'Email already registered.'}
    
    if User.query.filter_by(username=username).first():
        return {'error': 'Username already taken.'}
    
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, email=email, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    
    access_token = create_access_token(identity=new_user.id)
    return {'user': new_user.username, 'token': access_token}

def authenticate_user(email, password):
    """
    Authenticate user and return JWT if valid.
    :param email: User's email
    :param password: User's password
    :return: JWT token if valid
    """
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password_hash, password):
        if not getattr(user, 'is_active', True):
            return None  # Inactive accounts cannot login
        access_token = create_access_token(identity=user.id)
        return access_token
    return None
