
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "Elias Backend is running!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
