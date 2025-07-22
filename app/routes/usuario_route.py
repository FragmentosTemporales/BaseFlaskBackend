from flask import Blueprint, jsonify
from flask_jwt_extended import (
    get_jwt_identity,
    jwt_required,
    create_access_token
)
from app.models import *
from app.schemas import *


usuario = Blueprint("usuario", __name__)


@usuario.route("/usuario", methods=["GET"])
@jwt_required()
def get_usuarios() -> dict:
    """ Endpoint to get all usuarios """
    try:
        uid = get_jwt_identity()

        if not uid:
            return jsonify({"message": "Unauthorized access."}), 401

        data = Usuario.get_all()
        usuarios = usuarios_schema.dump(data)

        if not usuarios:
            return jsonify({"message": "No usuarios found."}), 404

        response = {
            "data": usuarios,
            "total": len(usuarios),
            "message": "Usuarios retrieved successfully."
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
