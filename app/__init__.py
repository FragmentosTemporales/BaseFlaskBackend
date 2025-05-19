from flask import Flask, jsonify
from .config import config
from .settings import settings as s
from .routes import jwt, main, cors
from .models import db, migrate


def create_app(test_mode=False):
    app = Flask(__name__, instance_relative_config=True)

    if test_mode:
        app.config.from_object(config["test"])
    else:
        env = s.flask_env
        app.config.from_object(config[env])

    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
    jwt.init_app(app)
    app.register_blueprint(main)

    @app.errorhandler(404)
    def page_not_found(error):
        return jsonify({"error": "Page not found"}), 404

    return app
