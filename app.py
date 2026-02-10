from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)  # Enable CORS

model = joblib.load('model.pkl')

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    try:
        features = [[data["age"], data["income"], data["education"]]]
    except KeyError:
        return jsonify({"error": "Missing keys in request"}), 400
    
    prediction = model.predict(features)[0]
    return jsonify({"party": prediction})

if __name__ == "__main__":
    app.run(debug=True)