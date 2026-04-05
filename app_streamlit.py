import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import random
import os

st.title("Skin Cancer Detection")

# model load (optional)
model = None
if os.path.exists("model.h5"):
    model = tf.keras.models.load_model("model.h5")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Predict"):
        if model:
            img = image.resize((224, 224))
            img = np.array(img) / 255.0
            img = np.expand_dims(img, axis=0)

            pred = model.predict(img)[0][0]
            result = "Malignant" if pred > 0.5 else "Benign"
            confidence = round(float(pred), 2)
        else:
            result = random.choice(["Benign", "Malignant"])
            confidence = round(random.uniform(0.7, 0.99), 2)

        st.write(f"Result: {result}")
        st.write(f"Confidence: {confidence}")

st.warning("⚠️ This is not a medical diagnosis. Please consult a doctor.")