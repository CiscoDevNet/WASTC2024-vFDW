from flask import Flask, jsonify, Blueprint, request, send_from_directory
import random
import os

app = Flask(__name__)

# Create a Blueprint named 'example'
example_bp = Blueprint("example", __name__)


# Define a route on the Blueprint
@example_bp.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, world!"})


# Define a calculator route
@example_bp.route("/calculate", methods=["GET"])
def calculate():
    operation = request.args.get("operation")
    x = float(request.args.get("x", 0))
    y = float(request.args.get("y", 0))
    if operation == "add":
        result = x + y
    elif operation == "subtract":
        result = x - y
    elif operation == "multiply":
        result = x * y
    elif operation == "divide":
        result = x / y if y != 0 else "undefined"
    else:
        return jsonify({"error": "Invalid operation"}), 400
    return jsonify({"result": result})


# Define a random quote route
quotes = [
    "Life is what happens when you're busy making other plans.",
    "Get busy living or get busy dying.",
    "The greatest glory in living lies not in never falling, but in rising every time we fall.",
    "The way to get started is to quit talking and begin doing.",
]


@example_bp.route("/quote", methods=["GET"])
def quote():
    return jsonify({"quote": random.choice(quotes)})


# Register the Blueprint with the main app
app.register_blueprint(example_bp, url_prefix="/api")


@app.route("/")
def index():
    return send_from_directory(os.path.abspath(""), "index.html")


# Ignore favicon.ico requests
@app.route("/favicon.ico")
def favicon():
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
