import os
import pickle
import pandas as pd
import streamlit as st
import signal
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from datetime import datetime

# === Rate Limiting ===
if "last_submit_time" not in st.session_state:
    st.session_state["last_submit_time"] = 0
cooldown = 10  # seconds

# === Timeout Handler ===
class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException

signal.signal(signal.SIGALRM, timeout_handler)

def predict_with_timeout(predict_fn, user_input, timeout=5):
    signal.alarm(timeout)
    try:
        result = predict_fn(user_input)
    finally:
        signal.alarm(0)
    return result

# === Load model and vectorizer ===
model_path = os.path.join("models", "scam_classifier.pkl")
vectorizer_path = os.path.join("models", "tfidf_vectorizer.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(vectorizer_path, "rb") as f:
    vectorizer = pickle.load(f)

# === Prediction function ===
def predict(text):
    transformed = vectorizer.transform([text])
    prediction = model.predict(transformed)
    return prediction[0]

# === Streamlit UI ===
st.set_page_config(page_title="Scam Message Detector", layout="centered")
st.title("🕵️ Scam Message Detector")
st.markdown("Enter a message to check if it's a **scam** or **not**.")

user_input = st.text_area("Enter your message here:", height=150)
submitted = st.button("Analyze")

now = datetime.now().timestamp()
last_submit = st.session_state.get("last_submit_time", 0)

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

st.markdown("---")
st.caption("Made by Michal · [GitHub](https://github.com/MikeMat22/scam-detector-nlp)")
