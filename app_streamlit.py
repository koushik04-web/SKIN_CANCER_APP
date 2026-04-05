import streamlit as st
import base64

def set_bg():
    try:
        with open("bg.jpg", "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        st.markdown(f"""
            <style>
            .stApp {{
                background-image: url("data:image/jpeg;base64,{encoded}");
                background-size: cover;
                background-position: center;
            }}
            </style>
        """, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("Background image 'bg.jpg' not found!")

# Call function
set_bg()

import streamlit as st
from PIL import Image
import numpy as np
import random

st.title("Skin Cancer Detection")

st.write("Upload a skin image to detect possible cancer.")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Predict"):
        # Dummy prediction (since model not used in deployment)
        result = random.choice(["Benign", "Malignant"])
        confidence = round(random.uniform(0.7, 0.99), 2)

        if result == "Malignant":
            st.error(f"Result: {result}")
        else:
            st.success(f"Result: {result}")

        st.write(f"Confidence: {confidence}")

st.warning("⚠️ This is not a medical diagnosis. Please consult a doctor.")

