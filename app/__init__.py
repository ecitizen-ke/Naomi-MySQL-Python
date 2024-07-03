from flask import Flask
from .view.state import state_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(state_bp)
    return app
