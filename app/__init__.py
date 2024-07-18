from flask import Flask
from .view.state import state_bp

def create_app():
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_pyfile("config.py")
    app.register_blueprint(state_bp,url_prefix="/api/v1/")
    return app
