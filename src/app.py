import streamlit as st
import pandas as pd
import joblib
import os
import time
import signal

# Load model and vectorizer
model = joblib.load(os.path.join("models", "logistic_model.pkl"))
vectorizer = joblib.load(os.path.join("models", "tfidf_vectorizer.pkl"))

# === Timeout support ===
class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException("Prediction timed out")

def predict_with_timeout(predict_fn, text, timeout=5):
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout)
    try:
        result = predict_fn(text)
    finally:
        signal.alarm(0)
    return result

def predict(text):
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]
    return prediction

# === UI ===
st.set_page_config(page_title="Scam Detector", page_icon="🔍")
st.title("🔍 Scam Message Detector")
st.markdown("Detect whether a message is a scam using a machine learning model.")

# === Rate limit: Simple version (1 request per 10 seconds) ===
now = time.time()
last_submit = st.session_state.get("last_submit_time", 0)
cooldown = 10

with st.form("scam_form"):
    user_input = st.text_area("Paste the message you received:", height=150)
    submitted = st.form_submit_button("Analyze")

if submitted:
    if not user_input.strip():
        st.warning("Please enter a message to analyze.")
    elif now - last_submit < cooldown:
        wait = int(cooldown - (now - last_submit))
        st.warning(f"Please wait {wait} more seconds before submitting again.")
    else:
        st.session_state["last_submit_time"] = now
        with st.spinner("Analyzing..."):
            try:
                result = predict_with_timeout(predict, user_input, timeout=5)
                if result == "scam":
                    st.error("⚠️ This message is likely a **SCAM**.")
                else:
                    st.success("✅ This message appears to be **not a scam**.")
            except TimeoutException:
                st.error("⏱️ The model took too long to respond. Please try again later.")
