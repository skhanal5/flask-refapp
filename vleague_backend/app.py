from flask import Flask

from vleague_backend.routes.valorant_route import valorant_bp


def create_app(test_config=None) -> Flask:
    app = Flask(__name__)

    if test_config is None:
        # load config
        pass
    else:
        app.config.update(test_config)

    app.register_blueprint(valorant_bp)
    return app
