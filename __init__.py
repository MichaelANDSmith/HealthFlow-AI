from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from celery import Celery
import os

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
celery = Celery(__name__, broker=os.environ.get('CELERY_BROKER_URL'))

def create_app():
    """
    Create and configure the Flask application
    """
    app = Flask(__name__)

    # Load configuration from the config.py file
    app.config.from_object('config.Config')

    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    celery.conf.update(app.config)

    # Register Blueprints (controllers)
    from .controllers.time_controller import bp as time_bp
    from .controllers.health_controller import bp as health_bp
    from .controllers.auth_controller import bp as auth_bp

    app.register_blueprint(time_bp)
    app.register_blueprint(health_bp)
    app.register_blueprint(auth_bp)

    return app

