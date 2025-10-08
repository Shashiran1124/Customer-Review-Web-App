from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Initialize SQLAlchemy (no app passed here yet)
db = SQLAlchemy()

def create_app():
    # Initialize Flask app
    app = Flask(__name__)
    app.config.from_object(Config)  # Load configuration settings

    # Initialize SQLAlchemy with the app
    db.init_app(app)

    # Import routes and models after initializing db
    with app.app_context():
        from app.routes import app_routes  # Import blueprint for routes
        app.register_blueprint(app_routes)  # Register the blueprint

        from app import models  # Import models here

    return app
