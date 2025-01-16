
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    try:
        return render_template("index.html")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api", methods=["POST"])
def api():
    try:
        data = request.json
        response = {"message": "Elias API received your data!", "data": data}
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
