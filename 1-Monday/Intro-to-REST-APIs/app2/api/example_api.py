from flask import Blueprint, jsonify

example_bp = Blueprint("example", __name__)


@example_bp.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, world!"})
