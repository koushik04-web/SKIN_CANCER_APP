from flask import Flask, request, jsonify, send_from_directory
from PIL import Image
import numpy as np
import random
import os

app = Flask(__name__)

# OPTIONAL: model load (jokhon model thakbe tokhon use korbi)
model = None
if os.path.exists("model.h5"):
    import tensorflow as tf
    model = tf.keras.models.load_model("model.h5")

# Home route → index.html show korbe
@app.route("/")
def home():
    return send_from_directory(".", "index.html")

# Image preprocess (model thakle use hobe)
def preprocess_image(image):
    image = image.resize((224, 224))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

# Predict route
@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["file"]
    image = Image.open(file)

    # Jodi model thake → real prediction
    if model:
        processed = preprocess_image(image)
        pred = model.predict(processed)[0][0]

        if pred > 0.5:
            result = "Malignant"
        else:
            result = "Benign"

        confidence = round(float(pred), 2)

    # Jodi model na thake → dummy prediction
    else:
        result = random.choice(["Benign", "Malignant"])
        confidence = round(random.uniform(0.7, 0.99), 2)

    return jsonify({
        "prediction": result,
        "confidence": confidence
    })

if __name__ == "__main__":
    app.run(debug=True)


    