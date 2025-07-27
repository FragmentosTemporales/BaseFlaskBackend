from flask import Flask, jsonify
from rich import print
from .config import config
from .models import db, migrate
from .routes import jwt, main, cors
from .routes.usuario_route import usuario


def create_app(test_mode=False):
    print("[bold green]Iniciando la aplicación.[/bold green]")

    app = Flask(__name__, instance_relative_config=True)

    if test_mode:
        app.config.from_object(config["test"])
        print("[bold yellow]Modo de prueba activado.[/bold yellow]")

    else:
        app.config.from_object(config["dev"])
        print("[bold yellow]Modo de producción activado.[/bold yellow]")

    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)
    jwt.init_app(app)
    app.register_blueprint(main)
    app.register_blueprint(usuario, url_prefix='/usuario')

    @app.errorhandler(404)
    def page_not_found(error):
        return jsonify({"error": "Page not found"}), 404

    return app
