from flask import Flask, jsonify
from .api.example_api import example_bp  # Adjusted the import

app = Flask(__name__)
app.register_blueprint(example_bp, url_prefix="/api")


@app.route("/")
def index():
    return jsonify({"message": "Welcome to the Intro to REST APIs workshop!"})


# Ignore favicon.ico requests
@app.route("/favicon.ico")
def favicon():
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
