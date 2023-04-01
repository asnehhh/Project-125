from flask import Flask, jsonify, request
from classifier4 import  get_prediction

app4 = Flask(__name__)

@app4.route("/predict-alphabet", methods=["POST"])
def predict_data():
  image = request.files.get("alphabet")
  prediction = get_prediction(image)
  return jsonify({
    "prediction": prediction
  }), 200

if __name__ == "__main__":
  app4.run(debug=True)