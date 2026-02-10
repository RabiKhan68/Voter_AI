from flask import Flask, request, jsonify
import joblib
from flask_cors import CORS   # <-- IMPORTANT

app = Flask(__name__)
CORS(app)   # <-- ALLOWS VERCEL

model = joblib.load('model.pkl')

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    features = [[data["age"], data["income"], data["education"]]]
    prediction = model.predict(features)[0]
    return jsonify({"party": prediction})

if __name__ == "__main__":
    app.run()