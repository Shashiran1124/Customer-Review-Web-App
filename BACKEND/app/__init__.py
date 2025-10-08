from flask import Flask
from .routes import app_routes

app = Flask(__name__)
app.config.from_object('config.Config')  # Load configuration from the config.py

app.register_blueprint(app_routes)  # Register API routes
