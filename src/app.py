import streamlit as st
import pandas as pd
import joblib
import os
import signal
from streamlit_extras.rate_limiter import rate_limit

# Load the model and vectorizer
model = joblib.load(os.path.join("models", "logistic_model.pkl"))
vectorizer = joblib.load(os.path.join("models", "tfidf_vectorizer.pkl"))

# Timeout handler
class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException("Prediction timed out")

# Function to make prediction with timeout
@rate_limit(limit=5, period=60)  # Max 5 requests per minute
def predict_with_timeout(predict_fn, text, timeout=5):
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout)
    try:
        result = predict_fn(text)
    finally:
        signal.alarm(0)
    return result

# Prediction logic
def predict(text):
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]
    return prediction

# UI
st.set_page_config(page_title="Scam Detector", page_icon="🔍")
st.title("🔍 Scam Message Detector")
st.markdown("Detect whether a message is a scam using a machine learning model.")

with st.form("scam_form"):
    user_input = st.text_area("Paste the message you received:", height=150)
    submitted = st.form_submit_button("Analyze")

if submitted:
    if not user_input.strip():
        st.warning("Please enter a message to analyze.")
    else:
        with st.spinner("Analyzing..."):
            try:
                result = predict_with_timeout(predict, user_input, timeout=5)
                if result == "scam":
                    st.error("⚠️ This message is likely a **SCAM**.")
                else:
                    st.success("✅ This message appears to be **not a scam**.")
            except TimeoutException:
                st.error("⏱️ The model took too long to respond. Please try again later.")
