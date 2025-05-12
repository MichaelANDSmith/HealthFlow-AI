from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User
from app import db
from flask_jwt_extended import create_access_token
# +++ Added new imports +++
from sqlalchemy.exc import SQLAlchemyError  # For database error handling
import re  # For email format validation

def register_user(username, email, password):
    """
    Register a new user and hash the password.
    :param username: User's username
    :param email: User's email address
    :param password: User's password
    :return: User object
    """
    # +++ Added input validation +++
    if len(password) < 8:
        return {'error': 'Password must be at least 8 characters long'}
    
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return {'error': 'Invalid email format'}
    
    existing_user = User.query.filter((User.email == email) | (User.username == username)).first()
    if existing_user:
        if existing_user.email == email:
            return {'error': 'Email already registered'}
        return {'error': 'Username already taken'}
    
    try:
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        access_token = create_access_token(identity=new_user.id)
        return {'user': new_user.username, 'token': access_token}
    
    # +++ Added database error handling +++
    except SQLAlchemyError as e:
        db.session.rollback()
        return {'error': 'Registration failed due to database error'}

def authenticate_user(email, password):
    """
    Authenticate user and return JWT if valid.
    :param email: User's email
    :param password: User's password
    :return: JWT token if valid
    """
    user = User.query.filter_by(email=email).first()
    
    # +++ Enhanced authentication checks +++
    if not user:
        return {'error': 'Invalid credentials'}
    
    if not check_password_hash(user.password_hash, password):
        return {'error': 'Invalid credentials'}
    
    # +++ Added explicit is_active check +++
    if hasattr(user, 'is_active') and not user.is_active:
        return {'error': 'Account deactivated'}
    
    try:
        access_token = create_access_token(identity=user.id)
        return {'token': access_token}
    
    # +++ Added general exception handling +++
    except Exception as e:
        return {'error': 'Authentication failed'}
