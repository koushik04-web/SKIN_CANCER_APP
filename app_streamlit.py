import streamlit as st
from PIL import Image
import random
import base64

# 🔥 Page config
st.set_page_config(layout="wide")

# 🔥 Background
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
            background-repeat: no-repeat;
        }}

        /* 🔥 Glass Card UI */
        .box {{
            background: rgba(255, 255, 255, 0.08);
            padding: 25px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.2);
        }}

        .box h3 {{
            color: #00BFFF;
        }}

        .box p {{
            color: white;
            font-size: 16px;
        }}

        </style>
        """, unsafe_allow_html=True)
    except:
        pass

set_bg()

# 🔵 TITLE
st.markdown("<h1 style='text-align: center; color:#00BFFF;'>Skin Cancer Detection</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color:white;'>Upload a skin image to detect possible cancer.</p>", unsafe_allow_html=True)

# 📤 Upload Section
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Predict"):
        result = random.choice(["Benign", "Malignant"])
        confidence = round(random.uniform(0.7, 0.99), 2)

        if result == "Malignant":
            st.error(f"⚠️ Malignant (Confidence: {confidence})")
        else:
            st.success(f"✅ Benign (Confidence: {confidence})")

st.warning("⚠️ This is not a medical diagnosis. Please consult a doctor.")

st.write("---")


c1, _ = st.columns([2, 6])
with c1:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown("<h3>🔍 Our Mission</h3>", unsafe_allow_html=True)
    st.markdown("<p>Our goal is to provide a fast and accessible AI-based system for detecting possible skin cancer.</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.write("")

# RIGHT CARD
_, c2 = st.columns([6, 2])
with c2:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown("<h3>🛠️ How it Works</h3>", unsafe_allow_html=True)
    st.markdown("<p>This system uses AI concepts to classify skin images.</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.write("")

# LEFT CARD
c3, _ = st.columns([2, 6])
with c3:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown("<h3>🚀 Future Updates</h3>", unsafe_allow_html=True)
    st.markdown("<p>Coming soon: real AI model, reports and doctor integration.</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
