# app.py
from flask import Flask, render_template, request, jsonify
from model import predict_oil_prices

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        inflation = float(request.form.get("inflation", 3.0))
        econ_challenges = int(request.form.get("econ_challenges", 5))
        policy_support = int(request.form.get("policy_support", 5))
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400

    forecasts = predict_oil_prices(
        start_year=2025,
        end_year=2075,
        inflation_rate=inflation,
        econ_challenge_level=econ_challenges,
        policy_support_level=policy_support,
    )

    return jsonify({"forecasts": forecasts})

if __name__ == "__main__":
    app.run(debug=True)
