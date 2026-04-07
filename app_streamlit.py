import streamlit as st
from PIL import Image
import random
import base64

# 🔥 Full width layout
st.set_page_config(layout="wide")

# 🔥 Background function
def set_bg():
    try:
        with open("bg.jpg", "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()

        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/jpeg;base64,{encoded}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
            }}

            .box {{
                background: rgba(0, 0, 0, 0.6);
                padding: 25px;
                border-radius: 15px;
                color: white;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except:
        pass

set_bg()

# 🔥 TITLE
st.markdown("<h1 style='text-align: center;'>Skin Cancer Detection</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Upload a skin image to detect possible cancer.</p>", unsafe_allow_html=True)

# 🔥 Upload Section
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

# =========================
# 🔥 ZIGZAG UI SECTION
# =========================

# --- CARD 1 (LEFT) ---
c1_left, c1_gap = st.columns([2, 6])
with c1_left:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown("### 🔍 Our Mission")
    st.write("Our goal is to provide a fast and accessible AI-based system for detecting possible skin cancer.")
    st.markdown('</div>', unsafe_allow_html=True)

st.write("")

# --- CARD 2 (RIGHT) ---
c2_gap, c2_right = st.columns([6, 2])
with c2_right:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown("### 🛠️ How it Works")
    st.write("This system uses AI concepts to classify skin images as benign or malignant.")
    st.markdown('</div>', unsafe_allow_html=True)

st.write("")

# --- CARD 3 (LEFT) ---
c3_left, c3_gap = st.columns([2, 6])
with c3_left:
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown("### 🚀 Future Updates")
    st.write("We plan to integrate real AI model, reports, and doctor suggestions.")
    st.markdown('</div>', unsafe_allow_html=True)
