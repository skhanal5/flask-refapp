from flask import Flask

from flask_refapp.routes.valorant import valorant_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(valorant_bp)
    return app
