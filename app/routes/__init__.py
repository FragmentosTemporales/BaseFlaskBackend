from flask import Blueprint, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager


jwt = JWTManager()
main = Blueprint("main", __name__)
cors = CORS(resources={r"/*": {"origins": "*"}})


@main.route("/")
def home():
    """ Home function """
    return jsonify({"message": "Welcome to the Flask API!"}), 200
