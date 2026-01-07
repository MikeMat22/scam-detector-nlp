import streamlit as st
import joblib
import re
import time
from PIL import Image
import numpy as np
import os

# Load the model and vectorizer
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "../models/logistic_model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "../models/tfidf_vectorizer.pkl"))

# Function to clean input text
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text

# Function to predict and return confidence score
def predict(text):
    cleaned = clean_text(text)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)[0]
    confidence = np.max(model.predict_proba(vectorized))
    return prediction, confidence

# Streamlit app configuration
st.set_page_config(page_title="Scam Detector", page_icon=":mag:")

# Display logo and title
logo = Image.open("assets/logo.png")
st.image(logo, width=200)
st.title(" Scam Message Detector")

# Custom CSS for styling
st.markdown("""
    <style>
        textarea {
            font-size: 1.05rem !important;
            resize: none !important;
            overflow: hidden !important;
        }
        .stButton > button {
            background-color: #1FA1FF;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 0.6em 1.2em;
            transition: 0.3s ease;
        }
        .stButton > button:hover {
            background-color: #0e87d4;
            transform: scale(1.03);
        }
    </style>
""", unsafe_allow_html=True)

# Text input area
st.markdown("###  Paste the message you received:")
user_input = st.text_area(
    "", 
    height=100, 
    placeholder="Enter suspicious message here...", 
    label_visibility="collapsed"
)

# Analyze button
st.markdown("###  Detect:")
analyze_col = st.columns([1, 3, 1])[1]  # center alignment for the button

with analyze_col:
    if st.button(" Analyze Message", use_container_width=True):
        with st.spinner("Analyzing..."):
            prediction, confidence = predict(user_input)
            time.sleep(1.2)

        # Display result with confidence score
        if prediction == "spam":
            st.error(f"🚨 Scam detected! Confidence: {confidence:.2f}")
            st.progress(int(confidence * 100))
        else:
            st.success(f"✅ Message seems safe. Confidence: {confidence:.2f}")
            st.progress(int(confidence * 100))

# Footer
st.markdown("---")
st.caption("Built by Michal · Logistic Regression · scikit-learn · Streamlit")