from flask import Blueprint, jsonify


usuario = Blueprint("usuario", __name__)


@usuario.route("/usuario" , methods=["POST"])
def create_usuario() -> dict:
    """ Endpoint to create a new usuario """
    return jsonify({"message": "Usuario created successfully!"}), 201