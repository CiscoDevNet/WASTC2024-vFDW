from flask import Flask, jsonify
from .api.example_api import example_bp  # Adjusted the import

# from .utils.data import get_sample_data

app = Flask(__name__)
app.register_blueprint(example_bp, url_prefix="/api")


@app.route("/")
def index():
    # Combine the welcome message and sample data into one JSON response
    return jsonify(
        {
            "message": "Welcome to the Intro to REST APIs workshop!",
            # "sample_data": get_sample_data(),
        }
    )


# Ignore favicon.ico requests
@app.route("/favicon.ico")
def favicon():
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
