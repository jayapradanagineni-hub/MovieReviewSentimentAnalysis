from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

model = joblib.load("sentiment_model.pkl")

@app.route("/")
def home():
    return "Movie Review Sentiment Analysis API is Running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    review = data.get("review", "")

    if not review.strip():
        return jsonify({"error": "Please enter a movie review"}), 400

    prediction = model.predict([review])[0]

    return jsonify({
        "review": review,
        "sentiment": prediction
    })

if __name__ == "__main__":
    app.run(debug=True)