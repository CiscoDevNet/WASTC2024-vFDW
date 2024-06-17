from flask import Flask, request, render_template, jsonify
from webhook_processor import process_webhook, get_processed_data

app = Flask(__name__)
app.config.from_pyfile("config.py")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json  # Assuming webhook data is JSON
    response = process_webhook(data)
    return jsonify(response), 200


@app.route("/webhook-data", methods=["GET"])
def webhook_data():
    data = get_processed_data()
    return jsonify(data), 200


if __name__ == "__main__":
    app.run(debug=True)
