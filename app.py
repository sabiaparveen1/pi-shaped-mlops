# app.py
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler at startup
model = joblib.load("model/iris_model.pkl")
scaler = joblib.load("model/scaler.pkl")

# Class labels
classes = ['setosa', 'versicolor', 'virginica']

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Iris Flower Prediction API",
        "endpoints": {
            "/": "API Info",
            "/health": "Health check",
            "/predict": "POST JSON with features to get predictions"
        }
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "OK"}), 200

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        features = data.get("features")

        if not features or len(features) != 4:
            return jsonify({"error": "Invalid input. Expecting 4 numeric features."}), 400

        features = np.array(features).reshape(1, -1)
        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)[0]
        predicted_class = classes[prediction]

        return jsonify({
            "prediction": predicted_class,
            "class_index": int(prediction)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

